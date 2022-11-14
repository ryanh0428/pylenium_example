from pylenium.driver import Pylenium

from tests.copart_com.pages.home_page import HomePage
from tests.copart_com.pages.search_result import SearchResultsPage


class CopartPages:
    def __init__(self,py:Pylenium):
        self.py=py
        self.home = HomePage(py)
        self.search_result = SearchResultsPage(py)

    def goto(self)->Pylenium:
        return self.py.visit("https://www.copart.co.uk/")