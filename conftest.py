import pytest
from selene import browser

@pytest.fixture(autouse=True)
def size_window():
    browser.config.window_width = 1280
    browser.config.window_height = 1024
    yield browser
    browser.quit()


@pytest.fixture(autouse=True)
def open(size_window):
    browser.open('https://google.com')
    yield
    browser.quit()

