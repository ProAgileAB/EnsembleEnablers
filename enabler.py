import json
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, List

md = str


@dataclass
class Enabler:
    name: str
    identifier: str
    also_known_as: Optional[str]
    symptoms: List[str]
    proposal: md

    @staticmethod
    def from_dict(enabler):
        name = enabler['name']
        identifier = id_from_name(name)
        symptoms = enabler['symptoms']
        proposal = enabler['proposal']
        aka = enabler.get('aka', None)
        return Enabler(name, identifier, aka, symptoms, proposal)


def load_enablers():
    path = ENABLERS_PATH
    text = path.read_text(encoding='utf8')
    raw_list = json.loads(text)
    for enabler in raw_list:
        proposal_path = Path(file_path_from_enabler_name(enabler['name']))
        print(f"Looking for {proposal_path}... ")
        if proposal_path.exists():
            print("\tFound it - using instead of field.")
            enabler['proposal'] = proposal_path.read_text(encoding='utf8')
    enabler_dto_list = [Enabler.from_dict(enabler) for enabler in raw_list]
    sorted_enablers = sorted(enabler_dto_list, key=lambda enabler: enabler.name)
    return sorted_enablers


def format_enablers(enablers, formatter):
    return ''.join(formatter(enabler) for enabler in enablers)


def file_path_from_enabler_name(enabler_name):
    return f"data/{id_from_name(enabler_name)}.md"


def id_from_name(enabler_name):
    return (enabler_name
            .lower()
            .replace(' ', '-')
            .replace('.', '')
            .replace(',', '')
            )


def enabler_self_tests():
    assert 'data/connect-first.md' == file_path_from_enabler_name("Connect first")
    assert 'connect-first' == id_from_name("Connect first")
    assert 'yes-and' == id_from_name("Yes, and...")


ENABLERS_PATH = Path('data/enablers.json')
