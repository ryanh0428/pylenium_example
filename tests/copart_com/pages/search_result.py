from pylenium.driver import Pylenium

from tests.copart_com.pages.page_base import PageBase


class SearchResultsPage(PageBase):
    def __init__(self,py:Pylenium):
        super().__init__(py)

    def click_classic_view_button(self):
        self.py.get("search-results-view-toggle").click()


    def click_show_number(self, num):
        self.py.get('select[name="serverSideDataTable_length"]').select_by_value(num)