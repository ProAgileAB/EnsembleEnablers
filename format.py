
from enabler import ENABLERS_PATH

replace = {
 "'": ["’"],
 r"\"": ["“", "”"]
}

if __name__ == '__main__':
    text = ENABLERS_PATH.read_text(encoding='utf8')
    for new, olds in replace.items():
        for old in olds:
            text = text.replace(old, new)
    ENABLERS_PATH.write_text(text, encoding='utf8')