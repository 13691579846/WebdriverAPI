# from selenium import webdriver
# import time
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('http://oatest.fandow.com')
# driver.implicitly_wait(2)
# driver.find_element_by_id('username').send_keys('fd-0002')
# driver.find_element_by_id('password').send_keys('123456')
# driver.find_element_by_id('login-action').click()
# driver.find_element_by_css_selector("a.welcome-close").click()
# driver.find_element_by_css_selector('i.times').click()
# time.sleep(2)
# elements = driver.find_elements_by_xpath("//div[@class='accordionHeader']/h2")
# time.sleep(2)
# for ele in elements:
#     if ele.text =='行政管理':
#         time.sleep(1)
#         ele.click()
# import sys
# print(sys.getdefaultencoding())
from selenium import webdriver
import unittest
class demo(unittest.TestCase):

    def setUp(self):
        self.a ='ss'
    def test_01(self):
        self.a = input('>>>')
        return self.a
    def test_02(self):
        print(self.test_01())

if __name__=='__main__':
    unittest.main()