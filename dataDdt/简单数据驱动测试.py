from selenium import webdriver
from ddt import ddt, data, unpack
import unittest
import time
from selenium.common.exceptions import NoSuchWindowException
'''
简单数据驱动测试
'''
@ddt
class ddtTest(unittest.TestCase):
    # 数据 可以是元祖， 列表， 字典（可迭代对象）
    value = [['13691579846@sohu.com', 'xiaochao11520','https://mail.sohu.com/fe/#/homepage'],
             ['13691579844@sohu.com', 'xiaochao11520','https://mail.sohu.com/fe/#/homepage']]
    # value = [{'uname':'13691579846@sohu.com', 'password':'xiaochao11520','expected':'https://mail.sohu.com/fe/#/homepage'},
    #          {'uname':'13691579844@sohu.com', 'password':'xiaochao11520','expected':'https://mail.sohu.com/fe/#/homepage'}]
    def setUp(self):
        self.testUrl = 'https://mail.sohu.com/fe/#/login'
        self.driver = webdriver.Firefox()
        self.driver.get(self.testUrl)

    @data(*value) # * 解析数据
    @unpack# 用来解包， 将每组数据的第一个数据传递给uname依次类推， 当数据为字典时，形参需和字段的key值相同
    def test_case1(self, uname, password, expected):
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
            print(e)
            raise
        except AssertionError:
            print('期望值是{}, 实际值是{}'.format(expected,currenturl))
            raise
        except Exception:
            raise
    def tearDown(self):
        self.driver.quit()
        # pass
if __name__ == '__main__':
    unittest.main()