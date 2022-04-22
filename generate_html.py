from pathlib import Path

import markdown

from enabler import load_enablers, format_enablers

HTML_PAGE = """<!doctype html>
<html lang="en">
<head>
    <title>Ensemble Enablers</title>
</head>
<body>
%s
</body>
</html>"""


def generate_html():
    body_content = html_content(load_enablers())
    text = HTML_PAGE % (body_content)
    HTML_OUTPUT_PATH.write_text(text, encoding='utf8')


def enabler_li(e):
    title = f"{e.name}"
    if e.proposal:
        title = f"<b>{title}</b>"
    return f" <li><a href='#{e.identifier}'>{title}</a>\n"


def html_content(enablers):
    result = "<h1>Ensemble enablers</h1>\n<ul>\n"
    result += format_enablers(enablers, enabler_li)
    result += "</ul>\n"
    result += format_enablers(enablers, enabler_as_html)
    return result


def enabler_as_html(enabler):
    header = f"\n<h1 id='{enabler.identifier}'>{enabler.name}</h1></a>\n\n"
    also_known_as = f"<i>Also known as: {enabler.also_known_as}</i>\n\n" if enabler.also_known_as else ''
    proposal = f"\n\n<h2>Proposal</h2>\n\n" + markdown.markdown(enabler.proposal)
    symptoms_list_items = ''.join(f" <li>{symptom}</li>\n" for symptom in enabler.symptoms)
    symptoms = f"<h2>Symptoms</h2>\n\n<ul>\n{symptoms_list_items}</ul>"
    return header + also_known_as + symptoms + proposal


HTML_OUTPUT_PATH = Path('index.html')
