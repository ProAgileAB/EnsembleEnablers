from pathlib import Path

import markdown

from enabler import load_enablers, format_enablers


def generate_html():
    text = html_content(load_enablers())
    HTML_OUTPUT_PATH.write_text(text, encoding='utf8')


def html_content(enablers):
    result = "<h1>Ensemble enablers</h1>\n<ul>\n"
    result += format_enablers(enablers,
                              lambda ix, e: f" <li><a href='#{ix}'>{e.name}</a>\n")
    result += "</ul>\n"
    result += format_enablers(enablers, enabler_as_html)
    return result


def enabler_as_html(ix, enabler):
    header = f"\n<h1 id='{ix}'>{enabler.name}</h1></a>\n\n"
    also_known_as = f"<i>Also known as: {enabler.also_known_as}</i>\n\n" if enabler.also_known_as else ''
    proposal = f"\n\n<h2>Proposal</h2>\n\n" + markdown.markdown(enabler.proposal)
    symptoms = f"<h2>Symptoms</h2>\n\n" + ''.join(f" <li>{symptom}</li>\n" for symptom in enabler.symptoms)
    return header + also_known_as + symptoms + proposal


HTML_OUTPUT_PATH = Path('index.html')
