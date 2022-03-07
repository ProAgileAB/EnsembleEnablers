# Uses the self-test idiom
import json

from pathlib import Path


def selftest():
    enablers = load_enablers()
    for enabler in enablers:
        assert enabler['name'], "Every enabler has a name"
        assert len(enabler['symptoms']) >= 1, "Every enabler has at least one symptom"
        assert enabler['proposal'], "Every enabler has a proposal"


def load_enablers():
    path = Path('enablers.json')
    text = path.read_text(encoding='utf8')
    return json.loads(text)


def generate():
    for enabler in load_enablers():
        name = enabler['name']
        symptoms = enabler['symptoms']
        proposal = enabler['proposal']
        aka = enabler.get('aka', None)
        print(f"# {name}\n")
        if aka:
            print(f"*Also known has: {aka}*\n")
        print(f"## Symptoms\n")
        for symptom in symptoms:
            print(f" * {symptom}")
        print(f"\n## Proposal\n")
        print(proposal)


if __name__ == '__main__':
    selftest()
    generate()
