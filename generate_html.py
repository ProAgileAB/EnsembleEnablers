from pathlib import Path

import markdown

from enabler import load_enablers, format_enablers

HTML_PAGE = """<!doctype html>
<html lang="en">
<head>
    <title>Ensemble Enablers</title>
    <link rel="stylesheet" href="https://unpkg.com/purecss@1.0.1/build/base-min.css">
    <style>
    body {
        background-color: lightblue;
    }
    .enabler {
        background-color: white;
        padding: 10px;
        margin: 10px;
        border: 2px solid gray;
        border-radius: 20px 50px;
        break-after: recto;
      }
    </style>
</head>
<body>
%s
</body>
<a href="https://github.com/ProAgileAB/EnsembleEnablers">See a mistake or have an enabler to add? Pull-requests are welcome <3</a>
</html>"""


HTML_PAGE_FOR_PRINT = """<!doctype html>
<html lang="en">
<head>
    <title>Ensemble Enablers</title>
    <link rel="stylesheet" href="https://unpkg.com/purecss@1.0.1/build/base-min.css">
    <style>
    .enabler {
        background-color: white;
        padding: 10px;
        margin: 10px;
        border: 2px solid gray;
        border-radius: 20px 50px;
        break-after: recto;
      }
    </style>
</head>
<body>
%s
</body>
</html>"""

def generate_html():

    # web version
    text = HTML_PAGE % html_content(load_enablers())
    HTML_OUTPUT_PATH.write_text(text, encoding='utf8')

    # for print version
    text = HTML_PAGE_FOR_PRINT % html_content(load_enablers(), for_print=True)
    HTML_FOR_PRINT_OUTPUT_PATH.write_text(text, encoding='utf8')


def enabler_li(e):
    title = f"{e.name}"
    if e.proposal:
        title = f"<b>{title}</b>"
    return f" <li><a href='#{e.identifier}'>{title}</a>\n"


def html_content(enablers, for_print=False):
    result = ''
    if not for_print:
        result = "<h1>Ensemble enablers</h1>\n<ul style='page-break-after: always;'>\n"
        result += format_enablers(enablers, enabler_li)
        result += "</ul>\n"
    result += format_enablers(enablers, enabler_as_html_for_print)
    return result


def enabler_as_html(enabler):
    header = f"\n<h1 id='{enabler.identifier}'>{enabler.name}</h1></a>\n\n"
    also_known_as = f"<i>Also known as: {enabler.also_known_as}</i>\n\n" if enabler.also_known_as else ''
    proposal = f"\n\n<h2>Proposal</h2>\n\n" + markdown.markdown(enabler.proposal)
    symptoms_list_items = ''.join(f" <li>{symptom}</li>\n" for symptom in enabler.symptoms)
    symptoms = f"<h2>Symptoms</h2>\n\n<ul>\n{symptoms_list_items}</ul>"
    return "<div class='enabler'>\n" + header + also_known_as + symptoms + proposal + "\n</div>\n\n"


def enabler_as_html_for_print(enabler):
    header = f"\n<h1 id='{enabler.identifier}'>{enabler.name}</h1></a>\n\n"
    also_known_as = f"<i>Also known as: {enabler.also_known_as}</i>\n\n" if enabler.also_known_as else ''
    proposal = f"\n\n<h2>Proposal</h2>\n\n" + markdown.markdown(enabler.proposal)
    symptoms_list_items = ''.join(f" <li>{symptom}</li>\n" for symptom in enabler.symptoms)
    symptoms = f"<h2>Symptoms</h2>\n\n<ul>\n{symptoms_list_items}</ul>"
    return "<div class='enabler'>\n" + also_known_as + symptoms + "<hr style=\"border-top: dotted 1px;\">" + header + proposal + "\n</div>\n\n"



HTML_OUTPUT_PATH = Path('index.html')

HTML_FOR_PRINT_OUTPUT_PATH = Path('index_for_print.html')
