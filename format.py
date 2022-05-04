from enabler import ENABLERS_PATH

replace = {
    "'": ["’"],
    r"\"": ["“", "”"]
}


def format_text(text):
    for new, olds in replace.items():
        for old in olds:
            text = text.replace(old, new)
    return text


def format_input_files():
    format_files([ENABLERS_PATH])


def format_files(format_paths):
    for path in format_paths:
        text = path.read_text(encoding='utf8')
        text = format_text(text)
        path.write_text(text, encoding='utf8')


if __name__ == '__main__':
    format_input_files()
