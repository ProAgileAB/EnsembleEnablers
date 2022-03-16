# Uses the self-test idiom
import json

from pathlib import Path

# TODO: Migrate JSON proposal field to use this path instead
def file_path_from_enabler_name(enabler_name):
    return f"proposals/{enabler_name.lower().replace(' ', '-')}.md"


def selftest():
    enablers = load_enablers()
    for enabler in enablers:
        assert enabler['name'], "Every enabler has a name"
        assert len(enabler['symptoms']) >= 1, "Every enabler has at least one symptom"
        assert enabler['proposal'], "Every enabler has a proposal"
    assert 'proposals/connect-first.md' == file_path_from_enabler_name("Connect First")


def load_enablers():
    path = ENABLERS_PATH
    text = path.read_text(encoding='utf8')
    return json.loads(text)


ENABLERS_PATH = Path('enablers.json')
OUTPUT_PATH = Path('README.md')
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


def generate():
    text = md_content(load_enablers())
    OUTPUT_PATH.write_text(text, encoding='utf8')


def md_content(enablers):
    result = PREAMBLE
    for enabler in enablers:
        name = enabler['name']
        symptoms = enabler['symptoms']
        proposal = enabler['proposal']
        aka = enabler.get('aka', None)
        result += f"# {name}\n\n"
        if aka:
            result += f"*Also known has: {aka}*\n\n"
        result += f"## Symptoms\n\n"
        for symptom in symptoms:
            result += f" * {symptom}\n"
        result += f"\n\n## Proposal\n\n"
        result += proposal
    return result


if __name__ == '__main__':
    print(file_path_from_enabler_name("Connect First"))
    selftest()
    generate()
