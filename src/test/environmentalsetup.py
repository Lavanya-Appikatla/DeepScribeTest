import datetime,json,re,os
from selenium import webdriver

class EnvironmentalSetup():
    global filepath
    filepath = re.escape(os.environ['PYTHONPATH'].split(os.pathsep)[0])
    with open(filepath+'\\Data\\data.json','r') as data:
        values = json.load(data)

    #setUp contains browser attributes
    def setUp(self):
        self.driver = webdriver.Chrome('C:\\Users\\tpusappi\\Downloads\\chromedriver_win32\\chromedriver.exe')
        print("Run started at :" +str(datetime.datetime.now()) )
        print("Chrome Environment Setup")
        print("......................................")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        return self.driver

    #tearDown contains browser closing attributes
    def tearDown(self):
        print("Run Completed at :" +str(datetime.datetime.now()))
        self.driver.close()
        self.driver.quit()

