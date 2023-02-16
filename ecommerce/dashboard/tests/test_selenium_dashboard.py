import pytest
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from django.contrib.auth.models import User

#@pytest.mark.selenium
#def test_create_new_admin_user(create_admin_user):
#    assert create_admin_user.__str__() == "admin"

@pytest.mark.selenium
def test_dashboard_admin_login(live_server, db_fixture_setup, firefox_browser_instance):

    i = User.objects.get(id=1)
    print(i.username)
    
    browser = firefox_browser_instance

    browser.get(f"{live_server.url}/admin/login/")

    #assert "Log in" in browser.page_source

    user_name = browser.find_element(By.NAME, "username")
    user_password = browser.find_element(By.NAME, "password")
    submit = browser.find_element(By.XPATH, '//input[@value="Log in"]')

    user_name.send_keys("root")
    user_password.send_keys("password")
    submit.send_keys(Keys.RETURN)
    sleep(5)

    assert "Site administration" in browser.page_source


