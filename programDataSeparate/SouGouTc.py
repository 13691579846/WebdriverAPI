from selenium import webdriver
import unittest
import time
from programDataSeparate.GetElement import getElement
class sogouTc(unittest.TestCase):

    def setUp(self):
        self.obj = getElement()
        self.driver = webdriver.Firefox()
        self.driver.get('http://www.sogou.com')
    def testSoGou(self):
        elementQuery = self.obj.getElement(self.driver, 'sogou', 'queryBox')
        elementQuery.send_keys('python')
        elementBtn = self.obj.getElement(self.driver, 'sogou', 'queryBtn')
        elementBtn.click()
        time.sleep(2)
        self.assertTrue('python' in self.driver.page_source)
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()