import json
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, List

md = str


@dataclass
class Enabler:
    name: str
    also_known_as: Optional[str]

    symptoms: List[str]
    proposal: md

    @staticmethod
    def from_dict(enabler):
        name = enabler['name']
        symptoms = enabler['symptoms']
        proposal = enabler['proposal']
        aka = enabler.get('aka', None)
        return Enabler(name, aka, symptoms, proposal)


def file_path_from_enabler_name(enabler_name):
    return f"enablers/{enabler_name.lower().replace(' ', '-')}.md"


def load_enablers():
    path = ENABLERS_PATH
    text = path.read_text(encoding='utf8')
    list_of_enablers = json.loads(text)
    list_of_enablers = sorted(list_of_enablers, key=lambda enabler: enabler['name'])
    return list_of_enablers


def format_enablers(enablers, formatter):
    return ''.join(formatter(ix, Enabler.from_dict(enabler))
                   for (ix, enabler) in enumerate(enablers))


ENABLERS_PATH = Path('enablers/enablers.json')


def enabler_self_test():
    enablers = load_enablers()
    for enabler in enablers:
        assert enabler['name'], "Every enabler has a name"
        assert len(enabler['symptoms']) >= 0, "Every enabler has a list of symptoms"
        assert "proposal" in enabler, "Every enabler has a proposal: " + str(enabler)
    assert 'enablers/connect-first.md' == file_path_from_enabler_name("Connect First")