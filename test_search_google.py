from selene import browser, have


def test_search():
    browser.element('[name="q"]').type('qa.guru').press_enter()
    browser.element('html').should(have.text('Об этой странице'))

def test_negative_search():
    browser.element('[name="q"]').type('!!!@3123123213333fdsfsd').press_enter()
    browser.element('html').should(have.text('Нет результатов для'))