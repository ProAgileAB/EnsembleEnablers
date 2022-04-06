from pathlib import Path

import markdown

from enabler import file_path_from_enabler_name, load_enablers, format_enablers


def generate_md():
    text = md_content(load_enablers())
    MD_OUTPUT_PATH.write_text(text, encoding='utf8')


def generate_html():
    text = html_content(load_enablers())
    HTML_OUTPUT_PATH.write_text(text, encoding='utf8')


# TODO: Migrate JSON proposal field to use this path instead




# Uses the self-test idiom


def self_test():
    enablers = load_enablers()
    for enabler in enablers:
        assert enabler['name'], "Every enabler has a name"
        assert len(enabler['symptoms']) >= 0, "Every enabler has a list of symptoms"
        assert "proposal" in enabler, "Every enabler has a proposal: " + str(enabler)
    assert 'enablers/connect-first.md' == file_path_from_enabler_name("Connect First")


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


def md_content(enablers):
    return PREAMBLE + format_enablers(enablers, enabler_as_markdown)


def enabler_as_markdown(_, e):
    md_string = f"# {e.name}\n\n"
    if e.also_known_as:
        md_string += f"*Also known has: {e.also_known_as}*\n\n"
    md_string += f"## Symptoms\n\n"
    for symptom in e.symptoms:
        md_string += f" * {symptom}\n"
    md_string += f"\n\n## Proposal\n\n"
    md_string += e.proposal
    return md_string


def enabler_as_html(ix, enabler):
    header = f"\n<h1 id='{ix}'>{enabler.name}</h1></a>\n\n"
    also_known_as = f"<i>Also known has: {enabler.also_known_as}</i>\n\n" if enabler.also_known_as else ''
    proposal = f"\n\n<h2>Proposal</h2>\n\n" + markdown.markdown(enabler.proposal)
    symptoms = f"<h2>Symptoms</h2>\n\n" + ''.join(f" <li>{symptom}</li>\n" for symptom in enabler.symptoms)
    return header + also_known_as + symptoms + proposal


def html_content(enablers):
    result = "<h1>Ensemble enablers</h1>\n<ul>\n"
    result += format_enablers(enablers,
                              lambda ix, e: f" <li><a href='#{ix}'>{e.name}</a>\n")
    result += "</ul>\n"
    result += format_enablers(enablers, enabler_as_html)
    return result


if __name__ == '__main__':
    print(file_path_from_enabler_name("Connect First"))
    self_test()
    generate_md()
    generate_html()
