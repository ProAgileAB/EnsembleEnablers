from approvaltests import verify, Options
from approvaltests.reporters import GenericDiffReporterFactory

from build import html_content, load_enablers


def test_html_generation():
    html = html_content(load_enablers())
    reporter = GenericDiffReporterFactory().get("meld")
    verify(html, options=Options().with_reporter(reporter))
