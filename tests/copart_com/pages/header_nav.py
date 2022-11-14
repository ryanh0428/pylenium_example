from pylenium.driver import Pylenium
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class HeaderNav():
    def __init__(self,py: Pylenium):
        self.py = py


    def search(self, query:str):
        self.py.get('#input-search').type(query, Keys.ENTER)

    def goto_how_it_work(self):
        button = self.py.wait(20).until(lambda x: x.find_element(By.CSS_SELECTOR,'a[href="./how-it-works"]')).click()
        button.click()
        # self.py.get('a[data-uname="howItWorks"]').click()
