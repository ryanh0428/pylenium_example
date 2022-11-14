from pylenium.driver import Pylenium

from tests.copart_com.pages.header_nav import HeaderNav


class PageBase:
    def __init__(self, py:Pylenium):
        self.py = py
        self.header = HeaderNav(py)