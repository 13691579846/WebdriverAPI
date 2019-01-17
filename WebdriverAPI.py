from selenium import webdriver
import unittest

class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    #1.访问具体地址2.获取当前页面url3.获取当前页面title

    def testOpenBaiduUrl(self):
        '''
        1.访问具体地址
        :return:
        '''
        baseUrl = 'https://www.baidu.com/'
        baseTitle = '百度一下'
        self.driver.get(baseUrl)
        currTitle = self.driver.title # 获取当前页面的标题
        self.assertIn(baseTitle, currTitle, msg='页面跳转失败')

    def testBackForwardRefresh(self):
        '''
        前进，后退，刷新当前页面
        :return:
        '''
        baseBaiduUrl = 'https://www.baidu.com/'
        baseSogouUrl = 'https://www.sogou.com/'
        self.driver.get(baseBaiduUrl)
        self.driver.get(baseSogouUrl)
        self.driver.back()
        self.assertIn(self.driver.current_url, baseBaiduUrl, msg='百度地址访问错误')
        print(self.driver.current_url)
        self.driver.forward()
        self.assertIn(self.driver.current_url, baseSogouUrl, msg='搜狗地址访问错误')
        print(self.driver.current_url)
        if self.driver.current_url == baseBaiduUrl:
            self.driver.find_element_by_id('kw').send_keys('baidu')
        else:
            self.driver.find_element_by_id('query').send_keys('sogou')
        self.driver.refresh()

    def testWindow(self):
        '''
        窗口最大化,获取当前窗口的位置，设置当前窗口的位置
        :return:
        '''
        baseBaiduUrl = 'https://www.baidu.com/'
        self.driver.get(baseBaiduUrl)
        position = self.driver.get_window_position()  # 获取当前窗口的位置坐标
        print('当前窗口的横坐标为{}'.format(position['x']))
        print('当前窗口的纵坐标为{}'.format(position['y']))
        self.driver.set_window_position(400, 200)
        print('设置后的窗口的位置坐标:{}'.format(self.driver.get_window_position()))
        self.driver.maximize_window() #窗口最大化

    def testWindowSize(self):
        '''
        获取当前窗口的大小，设置当前窗口的大小
        :return:
        '''
        baseBaiduUrl = 'https://www.baidu.com/'
        self.driver.get(baseBaiduUrl)
        #获取当前窗口的大小
        windowSize = self.driver.get_window_size('current')
        print('当前窗口的宽为{}'.format(windowSize['width']))
        print('当前窗口的高为{}'.format(windowSize['height']))
        #设置当前窗口的大小
        self.driver.set_window_size(width=200, height=400, windowHandle='current')
        print(self.driver.get_window_size('current'))
    def testGetBaiduTitle(self):
        '''
        获取页面的title属性值
        :return:
        '''
        baseBaiduUrl = 'https://www.baidu.com/'
        self.driver.get(baseBaiduUrl)
        bdTitle = self.driver.title
        print(bdTitle)
        self.assertEqual(bdTitle,'百度一下，你就知道',msg='页面title不正确')
    def testGetBaiduUrlSourceCode(self):
        '''
        获取页面的url和页面源码
        :return:
        '''
        baseBaiduUrl = 'https://www.baidu.com/'
        self.driver.get(baseBaiduUrl)
        bdUrl = self.driver.current_url # 获取当前页面的url地址
        print(bdUrl)
        self.assertEqual(bdUrl,'https://www.baidu.com/',msg='当前页面url不正确')
        sourceCode = self.driver.page_source
        print(sourceCode)
    def testGetwindowHandle(self):
        '''
        获取当前页面的句柄，切换窗口
        :return:
        '''
        import time
        baseBaiduUrl = 'https://www.baidu.com/'
        self.driver.get(baseBaiduUrl)
        self.driver.maximize_window()
        # 获取当前窗口句柄
        current_handle = self.driver.current_window_handle
        print(current_handle)
        #百度搜索框输入selenium并点击百度一下
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        time.sleep(3)
        #点击selenium的百度百科连接
        self.driver.find_element_by_partial_link_text('百度百科').click()
        #获取所有窗口的句柄
        all_handles = self.driver.window_handles
        print(all_handles)
        #打印新窗口的句柄
        print(self.driver.window_handles[-1])
        for handle in all_handles:
            # 切换到新的窗口
            if handle != current_handle:
                self.driver.switch_to.window(handle)
                self.driver.find_element_by_link_text('元素硒的英文名').click()
                # 返回到原来的窗口
                self.driver.switch_to.window(current_handle)
                sendKeys = self.driver.find_element_by_id('kw')
                sendKeys.clear()
                sendKeys.send_keys('python')
    def testGetElementInfo(self):

        baseBaiduUrl = 'https://www.baidu.com/'
        self.driver.get(baseBaiduUrl)
        self.driver.maximize_window()
        element = self.driver.find_element_by_xpath("//a[text()='新闻']")
        print('我的tag_name是{},我的text是{},我的size是{}'.format(element.tag_name,element.text,element.size))
    def testGetCssInfo(self):
        '''
        获取元素的css属性值
        :return:
        '''
        baseBaiduUrl = 'https://www.baidu.com/'
        self.driver.get(baseBaiduUrl)
        self.driver.maximize_window()
        element = self.driver.find_element_by_id('kw')
        print(element.value_of_css_property('height'))# 获取搜索框的高
        print(element.value_of_css_property('width'))# 获取搜索框的宽
        print(element.value_of_css_property('font-family'))# 获取搜索框输入的字体
    def testInputClear(self):
        '''
        获取元素的css属性值
        :return:
        '''
        import time
        baseBaiduUrl = 'https://www.baidu.com/'
        self.driver.get(baseBaiduUrl)
        self.driver.maximize_window()
        element = self.driver.find_element_by_id('kw')
        element.send_keys('python')# 输入指定内容
        time.sleep(5)
        element.clear() # 清空输入框
    def testElementIsDisplay(self):
        self.driver.get(r'file:///C:/Users/v-xug/Desktop/isdisplay.html')
        # 找到div2元素
        div2 = self.driver.find_element_by_id('div2')
        # 判断div2元素是否可见
        if div2.is_displayed():
            print('div2 元素可见')
        else:
            print('div2 元素不可见')
        # 点击第一个按钮
        button1 = self.driver.find_element_by_id('button1')
        button1.click()
        # 再次判断div2元素是否可见
        if div2.is_displayed():
            print('div2 元素可见')
        else:
            print('div2 元素不可见')
        #找到div4元素
        div4 = self.driver.find_element_by_id('div4')
        # 判断div4是否可见
        if div4.is_displayed():
            print('div4 元素可见')
        else:
            print('div4 元素不可见')
        # 点击第二个按钮
        button2 = self.driver.find_element_by_id('button2')
        button2.click()
        # 再次判断div4元素是否可见
        if div4.is_displayed():
            print('div4 元素可见')
        else:
            print('div4 元素不可见')
    def testElementIsEnable(self):
        self.driver.get(r'file:///C:/Users/v-xug/Desktop/isenable.html')
        input1 = self.driver.find_element_by_id('input1')
        if input1.is_enabled():
            print('input1 可操作')
        else:
            print('input1 不可操作')
        input2 = self.driver.find_element_by_id('input2')
        if input2.is_enabled():
            print('input2 可操作')
        else:
            print('input2 不可操作')
        input3 = self.driver.find_element_by_id('input3')
        if input3.is_enabled():
            print('input3 可操作')
        else:
            print('input3 不可操作')

    def testGetAttribute(self):
        self.driver.get('http://www.sogou.com')
        query = self.driver.find_element_by_id('query')
        print(query.get_attribute('name'))
        query.send_keys('python')
        print(query.get_attribute('value'))
    def testDoubleClick(self):
        from selenium.webdriver import ActionChains # 模拟鼠标操作事件包
        import time
        self.driver.get(r'file:///C:/Users/v-xug/Desktop/doubleclick.html')
        # 找到要操作的元素
        time.sleep(3)
        inputbox = self.driver.find_element_by_id('inputBox')
        action = ActionChains(self.driver)
        # 模拟鼠标双击操作
        action.double_click(inputbox).perform()
        time.sleep(3)
    # 遍历下拉列表，获取下拉列表元素的所有显示值和value属性值
    def testSelect(self):
        import time
        self.driver.get(r'file:///C:/Users/v-xug/Desktop/actionselect.html')
        # 查找下拉列表元素
        select = self.driver.find_element_by_name('fruit')
        elements = select.find_elements_by_xpath("//option")
        for element in elements:
            print(element.text)
            print(element.get_attribute('value'))
            element.click()
            time.sleep(1)
    def testSelectOption(self):
        import time
        from selenium.webdriver.support.ui import Select
        self.driver.get(r'file:///C:/Users/v-xug/Desktop/actionselect.html')
        select_element = Select(self.driver.find_element_by_xpath('//select'))
        # 打印默认选项
        print(select_element.first_selected_option.text)
        # 获取所有下拉选项元素
        all_options = select_element.options
        # 打印下拉选项的个数
        print(len(all_options))
        # 如果第二个选项可以操作且没有被选中，那么我们就选择这个选项
        if all_options[1].is_enabled() and not all_options[1].is_selected():
            # 第一个方法 通过序号选择选项 序号从0开始
            select_element.select_by_index(1)
            # 打印选中选项的文本
            print(select_element.all_selected_options[0].text)
        time.sleep(2)
        # 第二种办法通过选项的文本选择选项
        select_element.select_by_visible_text('猕猴桃')
        # 断言选中的选项是否为猕猴桃
        self.assertEqual(select_element.all_selected_options[0].text, '猕猴桃')
        time.sleep(2)

        # 第三种方法，通过选项的value属性值选择选项
        select_element.select_by_value('shanzha')
        print(select_element.all_selected_options[0].text)
        self.assertEqual(select_element.all_selected_options[0].text, '山楂')
    def testAssertOptions(self):

        from selenium.webdriver.support.ui import Select
        self.driver.get(r'file:///C:/Users/v-xug/Desktop/actionselect.html')
        select_element = Select(self.driver.find_element_by_xpath('//select'))
        # 找到所有的下拉选项
        actual_options = select_element.options
        # 期望列表
        expect_optionslist = ['桃子','西瓜','橘子','猕猴桃','山楂','荔枝']
        # 获取所有的选项的文本值
        actual_optionslist = [actual_options for actual_options in  map(lambda option:option.text, actual_options)]
        print(actual_optionslist)
        # 断言
        self.assertListEqual(expect_optionslist, actual_optionslist)
    def tearDown(self):
        # self.driver.quit()
        pass


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MyTest('testSelectOption'))
    runner = unittest.TextTestRunner()
    runner.run(suite)