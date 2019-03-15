from dataDdt.doXML import ParseXml
from selenium import webdriver
from selenium.common.exceptions import NoSuchWindowException, TimeoutException
import unittest
from ddt import ddt, data,unpack
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
values = ParseXml('./xmlData.xml')
@ddt
class xmltest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://mail.sohu.com/fe/#/login')
    @data(*values.getDataFromXml('book'))
    @unpack
    def test_xml(self,uname, password, expected):
        try:
            wait = WebDriverWait(self.driver,5)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='submit']")))
            username = self.driver.find_element_by_xpath("//input[@placeholder='请输入您的邮箱']")
            username.send_keys(uname)
            time.sleep(1)
            userpassword = self.driver.find_element_by_xpath("//input[@placeholder='请输入您的密码']")
            userpassword.send_keys(password)
            self.driver.find_element_by_xpath("//input[@type='submit']").click()
            time.sleep(2)
            currenturl = self.driver.current_url
            self.assertEqual(expected, currenturl, '登录失败')
        except TimeoutException as e:
            raise e
        except NoSuchWindowException as e:
            raise e
        except AssertionError as e:
            print('期望值是{}, 实际值是{}'.format(expected, currenturl))
            raise e
        except Exception:
            raise
    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main()