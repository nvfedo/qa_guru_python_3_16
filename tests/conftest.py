import pytest
from selene.support.shared import browser
from utils.base_session import demowebshop


@pytest.fixture(scope='session')
def register():
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.config.base_url = "https://demowebshop.tricentis.com/"
    response = demowebshop.post('/login', data={'Email': 'nvfedoqaguru3_16@mail.ru', 'Password': 'asdfgh'}, allow_redirects=False)
    authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")
    browser.open("Themes/DefaultClean/Content/images/logo.png")

    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": authorization_cookie})

    return browser
