from selenium import webdriver
from dataDdt.doExcel import excelData
import unittest,time
from ddt import ddt, data
from selenium.common.exceptions import NoSuchWindowException

excel = excelData('./dataexcel.xlsx', 'login')
@ddt
class excel_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://mail.sohu.com/fe/#/login')
    @data(*excel.read_excel())
    def test_excel(self, value):
        uname, password, expected = tuple(value)  # value是一个列表
        print(value)
        print(uname,password,expected)
        try:
            username = self.driver.find_element_by_xpath("//input[@placeholder='请输入您的邮箱']")
            username.send_keys(uname)
            time.sleep(1)
            userpassword = self.driver.find_element_by_xpath("//input[@placeholder='请输入您的密码']")
            userpassword.send_keys(password)
            self.driver.find_element_by_xpath("//input[@type='submit']").click()
            time.sleep(2)
            currenturl = self.driver.current_url
            self.assertEqual(expected, currenturl, '登录失败')
        except NoSuchWindowException as e:
            raise e
        except AssertionError as e:
            print('期望值是{}, 实际值是{}'.format(expected, currenturl))
            raise e
        except Exception:
            raise
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()