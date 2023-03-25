import pytest
from selenium import webdriver

@pytest.fixture(autouse=True, scope="function")
def testing():
    pytest.driver = webdriver.Chrome('C:\\Users\\ivash\PycharmProjects\\28\\tests\\chromedriver.exe')
    pytest.driver.implicitly_wait(10)
    pytest.driver.get('https://b2c.passport.rt.ru/')
    pytest.driver.set_window_size(1400, 1000)

    yield

    pytest.driver.quit()