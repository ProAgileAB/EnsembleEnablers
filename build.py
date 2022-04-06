import json
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, List

import markdown


@dataclass
class Enabler:
    name: str
    also_known_as: Optional[str]
    symptoms: List[str]
    proposal: str

    @staticmethod
    def from_dict(enabler):
        name = enabler['name']
        symptoms = enabler['symptoms']
        proposal = enabler['proposal']
        aka = enabler.get('aka', None)
        return Enabler(name, aka, symptoms, proposal)

# TODO: Migrate JSON proposal field to use this path instead


def file_path_from_enabler_name(enabler_name):
    return f"enablers/{enabler_name.lower().replace(' ', '-')}.md"


# Uses the self-test idiom
def self_test():
    enablers = load_enablers()
    for enabler in enablers:
        assert enabler['name'], "Every enabler has a name"
        assert len(enabler['symptoms']) >= 0, "Every enabler has a list of symptoms"
        assert "proposal" in enabler, "Every enabler has a proposal: " + str(enabler)
    assert 'enablers/connect-first.md' == file_path_from_enabler_name("Connect First")


def load_enablers():
    path = ENABLERS_PATH
    text = path.read_text(encoding='utf8')
    list_of_enablers = json.loads(text)
    list_of_enablers = sorted(list_of_enablers, key=lambda enabler: enabler['name'])
    return list_of_enablers


ENABLERS_PATH = Path('enablers/enablers.json')
MD_OUTPUT_PATH = Path('README.md')
HTML_OUTPUT_PATH = Path('index.html')
PREAMBLE = """
# Ensemble Enablers - what is this repo?

This repo documents patterns we've found useful while
coaching teams in Ensemble Programming.


## I want to update the README

Please do not update this README, instead modify
`enablers.json`. If you see some error in these
general instructions, modify `build.py` which
contain this pre-amble.


## How to add an enabler?

Update the enablers.json file, then run this command:

    python build.py

This will update README.md if no obvious errors were
found in enablers.json.

# ENSEMBLE ENABLERS BELOW

"""


def generate_md():
    text = md_content(load_enablers())
    MD_OUTPUT_PATH.write_text(text, encoding='utf8')


def generate_html():
    text = html_content(load_enablers())
    HTML_OUTPUT_PATH.write_text(text, encoding='utf8')


def md_content(enablers):
    result = PREAMBLE
    for e in map(Enabler.from_dict, enablers):
        result += f"# {e.name}\n\n"
        if e.also_known_as:
            result += f"*Also known has: {e.also_known_as}*\n\n"
        result += f"## Symptoms\n\n"
        for symptom in e.symptoms:
            result += f" * {symptom}\n"
        result += f"\n\n## Proposal\n\n"
        result += e.proposal
    return result


def html_content(enablers):
    result = "<h1>Ensemble enablers</h1>\n<ul>\n"
    for ix, enabler in enumerate(enablers):
        name = enabler['name']
        result += f" <li><a href='#{ix}'>{name}</a>\n"
    result += "</ul>\n"
    for ix, enabler in enumerate(enablers):
        name = enabler['name']
        symptoms = enabler['symptoms']
        proposal = enabler['proposal']
        proposal = markdown.markdown(proposal)
        aka = enabler.get('aka', None)
        result += f"\n<h1 id='{ix}'>{name}</h1></a>\n\n"
        if aka:
            result += f"<i>Also known has: {aka}</i>\n\n"
        result += f"<h2>Symptoms</h2>\n\n"
        for symptom in symptoms:
            result += f" <li>{symptom}</li>\n"
        result += f"\n\n<h2>Proposal</h2>\n\n"
        result += proposal
    return result


if __name__ == '__main__':
    print(file_path_from_enabler_name("Connect First"))
    self_test()
    generate_md()
    generate_html()
