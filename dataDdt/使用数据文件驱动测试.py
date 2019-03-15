from selenium import webdriver
from ddt import ddt, file_data
import unittest, time
from selenium.common.exceptions import NoSuchWindowException
import HTMLTestRunner
'''
从文件中读测试数据
'''

@ddt # ddt装饰测试类
class Testdata(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://mail.sohu.com/fe/#/login')

    @file_data('test_data.json') # 读取文件的 文件中数据可以是一个列表，也可以是一个字典
    def test_data(self,value):
        uname, password, expected = tuple(value.strip().split('||')) # value是一个字符串
        # print(type(value),value)
        try:
            username = self.driver.find_element_by_xpath("//input[@placeholder='请输入您的邮箱']")
            username.send_keys(uname)
            time.sleep(1)
            userpassword = self.driver.find_element_by_xpath("//input[@placeholder='请输入您的密码']")
            userpassword.send_keys(password)
            self.driver.find_element_by_xpath("//input[@type='submit']").click()
            time.sleep(2)
            currenturl = self.driver.current_url
            self.assertEqual(expected, currenturl,'登录失败')
        except NoSuchWindowException as e:
            raise e
        except AssertionError:
            print('期望值是{}, 实际值是{}'.format(expected,currenturl))
            raise
        except Exception:
            raise

    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()
    # import os
    # from datetime import date
    # currentPath = os.path.dirname(os.path.abspath(__file__))# 获取当前文件目录
    # reportPath = os.path.join(currentPath,'report') # 创建一个report目录
    # if not os.path.exists(reportPath):
    #     os.mkdir(reportPath) # 判断目录是否存在， 不存在就创建
    # reportName = os.path.join(reportPath, str(date.today())+'report.html') # 拼接html报告
    # with open(reportName,'wb') as f:
    #     suite = unittest.TestLoader().loadTestsFromTestCase(Testdata)
    #     runner = HTMLTestRunner.HTMLTestRunner(stream=f,verbosity=1, title='数据驱动测试报告', description='数据驱动')
    #     runner.run(suite)