import time,os,json
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

filepath = os.environ['PYTHONPATH'].split(os.pathsep)[0]

class BrowsePage():
    def __init__(self, driver):
        self.driver = driver
        global history,physicalExamination,lesion,blue,scaling,subscaling,color,diagnoses_btn
        global diagno,icd_no,size,diagnosesIcon_id
        global actions

        self.history_id ='encounterTab_2'
        self.physicalExamination_id = 'encounterTab_3'
        self.scrollBar_id = 'lftContainer'
        self.diagnosesIcon_id = 'encounterTab_6'
        self.diagnosis_id = 'diagnosis_0'
        self.icd_id = 'code_0'

        #
        with open(filepath+'\\data\\data.json','r') as data:
            values = json.load(data)
        history = values['TESTDATA']['History of Present Illness']
        physicalExamination = values['TESTDATA']['Physical Examination']['Template']
        scaling = values ['TESTDATA']['Physical Examination']['Checkboxes'][0]
        subscaling = values ['TESTDATA']['Physical Examination']['Checkboxes'][1]
        blue = values ['TESTDATA']['Physical Examination']['Checkboxes'][1][2]
        lesion = values ['TESTDATA']['Physical Examination']['Checkboxes'][1][0]
        color = values ['TESTDATA']['Physical Examination']['Checkboxes'][1][1]
        size = values ['TESTDATA']['Physical Examination']['Values']['Hypomelanotic Size']
        diagnoses_btn = values ['TESTDATA']['Diagnoses']
        diagno = values ['TESTDATA']['Diagnoses'][0]['Diagnosis']
        icd_no = values ['TESTDATA']['Diagnoses'][0]['Code']

    def click_chartnotes(self):
        elementtobepresent=self.driver.find_element_by_xpath("//i[@class='charts-menu-icon']")
        ActionChains(self.driver).move_to_element(elementtobepresent).click(elementtobepresent).perform()
        time.sleep(12)
    #
    def click_title(self):
        self.driver.find_element_by_xpath("//td[text()='Aug 03, 2020 : Dr.DeepScribe Dev : New Patient Visit : In Person']").click()
        time.sleep(3)


    def click_editchartnotes(self):
        self.driver.find_element_by_xpath("//button[text()='Edit']").click()
        time.sleep(3)
        self.driver.find_element_by_id(self.history_id).click()
        time.sleep(2)
        # self.driver.find_element_by_xpath(".//div[@id='editor_2']/div[@class ='ze']/iframe").clear()
        self.driver.find_element_by_xpath(".//div[@id='editor_2']/div[@class ='ze']/iframe").send_keys(history)
        time.sleep(2)
        self.driver.find_element_by_id(self.physicalExamination_id).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(".//td[@class='EncotdcommDiv']/div[@class='v1-chartnote-link']/div[text()='Templates']").click()
        time.sleep(3)
        actions = ActionChains(self.driver)
        scroll = self.driver.find_element_by_id(self.scrollBar_id)
        time.sleep(3)
        scroll.click()
        actions.send_keys(Keys.END).perform()
        time.sleep(2)
        target  = self.driver.find_element_by_xpath("//li[text()='"+physicalExamination+"']")
        target.click()

    def click_checkboxes(self):
        time.sleep(2)
        self.driver.find_element_by_xpath("//span[text()='IM Skin Growth - PE']")
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.END).perform()
        self.driver.find_element_by_xpath("//label[text()='"+lesion+"']").click()
        time.sleep(2)
        actions.send_keys(Keys.END).perform()
        self.driver.find_element_by_xpath("//label[text()='"+color+"']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//label[text()='"+blue+"']").click()
        time.sleep(5)
        actions.send_keys(Keys.END).perform()
        time.sleep(10)
        count = self.driver.find_elements_by_xpath("//input[@id='VALUE_569635000000029581']")
        print("count length:",len(count))
        # count.send_keys(size)
        element_size = count[0]
        element_size.send_keys(size)
        element_number = count[1]
        element_number.send_keys("test")
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[text()='OK']").click()

    def check_diagnosis(self):
        time.sleep(5)
        self.driver.find_element_by_id(self.diagnosesIcon_id).click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[text()='Add Dx']").click()
        time.sleep(3)
        self.driver.find_element_by_id(self.diagnosis_id).send_keys(diagno)
        time.sleep(2)
        self.driver.find_element_by_xpath("//span[text()='Benign hypertension']").click()
        time.sleep(2)
        # self.driver.find_element_by_id(self.icd_id).click()
        # self.driver.find_element_by_id(self.icd_id).send_keys(icd_no)
        # time.sleep(2)
        self.driver.find_element_by_xpath("//button[text()='Add']").click()
        time.sleep(2)
