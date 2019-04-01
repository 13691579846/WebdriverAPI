# from selenium import webdriver
# import time
# from selenium.webdriver import ActionChains
#
#
#
# driver = webdriver.Firefox()
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
# # elements = driver.find_elements_by_xpath('//*[@id="mCSB_3_container"]/ul[1]/ul[1]')
# # time.sleep(2)
# # for ele in elements:
# #     if ele.text == "用印申请":
# #         time.sleep(1)
# #         ele.click()
# time.sleep(2)
# ele = driver.find_element_by_xpath("//div[@class='gridTbody']/table/tbody/tr[1]")
# time.sleep(1)
# action = ActionChains(driver)
# action.click(ele).perform() # 选中第一行数据
# btn = driver.find_element_by_xpath("//ul[@class='toolBar']/li[5]")
# btn.click() # 点击删除
# time.sleep(1)
# alert = driver.find_element_by_xpath("//a[@class='button']")
# alert.click()

# print(tuple([i//2 for i in (200, 400)]))
#反转列表['p','y','t','h','o','n']

# import pymysql
#
# db = pymysql.connect("localhost", "root", "xiaochao11520", "mysql_test")
# cursor = db.cursor()
# cursor.execute("SELECT * FROMli")
# data = cursor.fetchone()
#
# print(data)
# db.close()

from selenium import webdriver
import unittest

class TestBaidu(unittest.TestCase):
    a =1

    def setUp(self):
        pass

    @unittest.skipIf(a>1, '跳过')
    def test_1(self):
        print('test1')
    def test_2(self):
        print('test2')
    def tearDown(self):
        pass
if __name__=='__main__':
    suite = unittest.defaultTestLoader.discover('.', pattern='test.py')
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)