from selenium.webdriver import Keys


def test_google_search(py):
    py.visit('https://google.com')
    py.get('[class="QS5gu sy4vM"]').click()
    py.get('[name="q"]').type('puppies', Keys.ENTER)
    assert py.should().contain_title('puppies')
