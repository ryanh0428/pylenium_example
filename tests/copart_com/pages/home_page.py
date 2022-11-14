from tests.copart_com.pages.page_base import PageBase


class HomePage(PageBase):
    def __init__(self,py):
        super().__init__(py)

    def go_to_how_it_work(self):
        self.header.goto_how_it_work()