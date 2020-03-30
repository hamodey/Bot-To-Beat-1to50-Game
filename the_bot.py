from selenium import webdriver
import time

class GameBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://zzzscore.com/1to50/en/?ts=1585578322745")
        time.sleep(5)

        elem = self.driver.find_element_by_id("grid")
        self.runGame(elem)
        time.sleep(10)

    def runGame(self, parent):
        for i in range(1, 51):
            #elem = self.driver.find_element_by_id("grid")
            
            child_elem = parent.find_element_by_xpath('//div[text() = "'+ str(i) + '"]')
            print(child_elem.text)
            child_elem.click()
        
            # elem = parent.find_element_by_xpath("//span[contains(text(), '1')]")
            # print(elem.text)
GameBot()
