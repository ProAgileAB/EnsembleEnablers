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
    pass


if __name__ == '__main__':
    selftest()
    generate()
