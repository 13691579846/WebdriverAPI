from selenium.webdriver.support.ui import WebDriverWait
import configparser
import os
from selenium import webdriver
class getElement():
    '''
    从配置文件中来获取定位信息
    '''
    def __init__(self):
        self.elementIni = os.path.dirname(os.path.abspath(__file__))\
                          +r'\WebElement.ini'
    def getElement(self, driver, sogouSection, sogouOption):
        try:
            f = configparser.ConfigParser()
            f.read(self.elementIni)
            locators = f.get(sogouSection, sogouOption).split(':')
            # 定位方式
            locaMethod = locators[0]
            # 定位表达式
            locaExpression = locators[1]
            # 通过显示等待的方式获取页面的元素
            element = WebDriverWait(driver,5).until(lambda x : x.find_element(locaMethod, locaExpression))
        except Exception as e:
            raise e
        else:
            return element

if __name__ == '__main__':
    ele = getElement()
    print(ele.elementIni)
    driver = webdriver.Firefox()
    driver.get('http://www.sogou.com')
    element = ele.getElement(driver, 'sougou', 'queryBox')
    element.send_keys('python')