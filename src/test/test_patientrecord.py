from src.test.environmentalsetup import EnvironmentalSetup
from src.pages.loginpage import LoginPage
from src.pages.browsepage import BrowsePage


class Test_Patientrecord():
    def test_patient_record(self):
        env_obj = EnvironmentalSetup()
        driver = env_obj.setUp()
        login = LoginPage(driver)
        browse = BrowsePage(driver)

        login.site_login()
        login.sign_in()
        login.enter_username()
        login.enter_password()
        login.check_keepSigned()
        login.submit_login()
        login.close_popup()

        browse.click_chartnotes()
        browse.click_title()
        browse.click_editchartnotes()
        browse.click_chartnotes()
        browse.click_checkboxes()
        browse.check_diagnosis()

        # env_obj.tearDown()