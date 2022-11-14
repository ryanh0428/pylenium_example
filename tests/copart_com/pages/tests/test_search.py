from tests.copart_com.pages.search_result import SearchResultsPage


def test_search_exotics(py,copart):
    copart.goto()
    copart.home.header.search('exotics')
    assert py.contains('PORSCH')


def test_show_number(py,copart):
    copart.goto()
    copart.home.header.search('exotics')
    copart.search_result.click_classic_view_button()
    copart.search_result.click_show_number("100")