import time,os,json

filepath = os.environ['PYTHONPATH'].split(os.pathsep)[0]

class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        global url
        global username,password,signIn

        self.username_id = 'lid'
        self.password_id = 'pwd'
        self.login_id = 'signin_submit'
        self.closeIcon_id ='NEW_DIALOG_CLOSE_MARK'
        #
        with open(filepath+'\\data\\data.json','r') as data:
            values = json.load(data)
        username = values['TESTDATA']['USER-DETAILS']['site_username']
        password = values['TESTDATA']['USER-DETAILS']['site_password']
        url = values['TESTDATA']['URL']['SITE-URL']

    def site_login(self):
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(5)

    def sign_in(self):
        self.driver.find_element_by_xpath("//span[@class = 'signin-button']").click()
        time.sleep(5)
    #
    def enter_username(self):
        self.driver.find_element_by_id(self.username_id).clear()
        self.driver.find_element_by_id(self.username_id).send_keys(username)

    def enter_password(self):
        self.driver.find_element_by_id(self.password_id).clear()
        self.driver.find_element_by_id(self.password_id).send_keys(password)

    def check_keepSigned(self):
        keep_me = self.driver.find_element_by_xpath("//span[@id='keepme']")
        if keep_me.get_attribute('checked')=='true':
            keep_me.click()
        else:
            return False

    #
    def submit_login(self):
        self.driver.find_element_by_id(self.login_id).click()
        time.sleep(3)

    def close_popup(self):
        self.driver.find_element_by_id(self.closeIcon_id).click()