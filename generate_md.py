from pathlib import Path

from enabler import load_enablers, format_enablers


def generate_md():
    text = md_content(load_enablers())
    MD_OUTPUT_PATH.write_text(text, encoding='utf8')


MD_OUTPUT_PATH = Path('README.md')


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


PREAMBLE = """
# Ensemble Enablers - what is this repo?

This repo documents patterns we've found useful while
coaching teams in Ensemble Programming.


## I want to update the README

Please do not update this README, instead modify
`enablers.json`. If you see some error in these
general instructions, modify `main.py` which
contain this pre-amble.


## How to add an enabler?

Update the enablers.json file, then run this command:

    python main.py

This will update README.md if no obvious errors were
found in enablers.json.

# ENSEMBLE ENABLERS BELOW

"""