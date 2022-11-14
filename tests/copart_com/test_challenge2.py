from selenium.webdriver import Keys

from tests.copart_com.pages.header_nav import HeaderNav


def test_challenge2(py,copart):
    py.get('#input-search').type('exotics', Keys.ENTER)
    assert py.contains('PORSCHE')
    headernav = HeaderNav(py)
    headernav.goto_how_it_work()