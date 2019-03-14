from selenium import webdriver
import unittest, os
from takeScreenShot.createDir import createDir

# 封装截图函数

picDir = createDir()
def takeScreenShot(driver, savepath, imagename):
    imagePath = os.path.join(savepath, imagename+'.png')
    try:
        driver.get_screenshot_as_file(imagePath)
    except Exception as e:
        raise e

class screenShot(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_screenshot(self):
        self.driver.get('http://www.baidu.com')
        title = self.driver.title
        try:
            self.assertEqual('百度一下你就知道', title, '断言失败')
        except AttributeError as e:
            takeScreenShot(self.driver, picDir,'failed1')
        except Exception as e:
            takeScreenShot(self.driver, picDir,'failed3')
            raise
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()