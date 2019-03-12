from selenium import webdriver
import unittest
'''
常用webdriverApi 详解（基础部分）
'''
class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    #1.访问具体地址2.获取当前页面url3.获取当前页面title
    """
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
        '''
        判断元素是否可见
        :return:
        '''
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
        '''
        判断元素是否可操作
        :return:
        '''
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
        '''
        获取元素属性值
        :return:
        '''
        self.driver.get('http://www.sogou.com')
        query = self.driver.find_element_by_id('query')
        print(query.get_attribute('name'))
        query.send_keys('python')
        print(query.get_attribute('value'))
    def testDoubleClick(self):
        '''
        模拟鼠标双击事件
        :return:
        '''
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
        '''
        操作select下拉列表元素
        :return:
        '''
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
    def testMultipleOptions(self):
        from selenium.webdriver.support.ui import Select
        import time
        self.driver.get(r'file:///C:/Users/v-xug/Desktop/multipleOptions.html')
        select_element = Select(self.driver.find_element_by_xpath('//select'))
        # 通过序号选择第一个元素
        select_element.select_by_index(0)
        # 通过文本选择山楂
        select_element.select_by_visible_text('山楂')
        # 通过选项的value属性值选择value=猕猴桃
        select_element.select_by_value('nihoutao')
        # 打印所有选中文本
        for option in select_element.all_selected_options:
            print(option.text)
        # 再次选中3个选项
        select_element.select_by_index(1)
        select_element.select_by_value('juzi')
        select_element.select_by_visible_text('荔枝')
        # 取消3个选项
        select_element.deselect_by_index(0)
        select_element.deselect_by_value('nihoutao')
        select_element.deselect_by_visible_text('山楂')
    def testInputSelect(self):
        self.driver.get(r'file:///C:/Users/v-xug/Desktop/inputselect.html')
        from selenium.webdriver.common.keys import Keys
        inputselect = self.driver.find_element_by_id('select')
        inputselect.clear()
        import time
        time.sleep(1)
        # 输入的同时按下箭头键
        inputselect.send_keys('c', Keys.ARROW_DOWN)
        time.sleep(1)
        inputselect.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        inputselect.send_keys(Keys.ENTER)
        time.sleep(3)

    def testRadio(self):
        import time
        self.driver.get(r'file:///C:/Users/v-xug/Desktop/radio.html')
        # 定位到草莓选项
        time.sleep(2)
        berry = self.driver.find_element_by_xpath("//input[@value='berry']")
        berry.click()
        # 断言是否被选中
        self.assertTrue(berry.is_selected())

        if berry.is_selected():
            # 如果被选中了重新选择西瓜选项
            watermelon = self.driver.find_element_by_xpath("//input[@value='watermelon']")
            watermelon.click()
            # 断言草莓未被选中
            self.assertFalse(berry.is_selected())
            # 查找所有的选项
            options = self.driver.find_elements_by_xpath("//input[@name='fruit']")
            # 遍历所有的选项，如果找到orange且未被选中，那么就选中这项
            for option in options:
                if option.get_attribute('value')=='orange':
                    if not option.is_selected():
                        option.click()
    def testCheckBox(self):
        self.driver.get(r'file:///C:/Users/v-xug/Desktop/checkbox.html')
        # 选中一个选项并取消
        berry = self.driver.find_element_by_xpath("//input[@value='berry']")
        berry.click()
        # 断言是否被选中
        self.assertTrue(berry.is_selected())
        # 取消选中
        if berry.is_selected():
            berry.click()
        # 遍历所有的选项并选中所有的选项
        options = self.driver.find_elements_by_xpath("//input[@name='fruit']")
        for option in options:
            if not option.is_selected():
                option.click()
    def testAssertIn(self):
        self.driver.get('http://www.baidu.com')
        self.driver.find_element_by_id('kw').send_keys('linux超')
        self.driver.find_element_by_id('su').click()
        import time
        time.sleep(4)
        self.assertIn('linux超', self.driver.page_source, msg='页面源码中不存在该关键字')

    def testScreenShot(self):
        '''
        页面截图操作
        :return:
        '''
        self.driver.get('http://www.baidu.com')
        try:
            # 使用get_screenshot_as_file(filename)方法，对浏览器当前打开的页面截图，并保存在当前目录下
            self.driver.get_screenshot_as_file('baidu.png')
        except IOError as e:
            print(e)
    def testDragDrop(self):
        '''
        模拟鼠标拖拽
        :return:
        '''
        import time
        self.driver.get(r'http://jqueryui.com/resources/demos/draggable/scroll.html')
        element1 = self.driver.find_element_by_id('draggable')
        element2 = self.driver.find_element_by_id('draggable2')
        element3 = self.driver.find_element_by_id('draggable3')
        from selenium.webdriver import ActionChains
        action = ActionChains(self.driver)
        # 把第一个元素拖拽到第二个元素的位置
        action.drag_and_drop(element1, element2).perform()
        # 把第三个元素拖拽10个像素，拖拽2次
        for i in range(2):
            action.drag_and_drop_by_offset(element3,10,10).perform()
            time.sleep(2)
        action.release()
    def testSingleKey(self):
        import time
        self.driver.get('http://www.sogou.com')
        query = self.driver.find_element_by_id('query')
        # 导入模拟按键模块
        from selenium.webdriver.common.keys import Keys
        # 输入框发送一个f12按键
        query.send_keys(Keys.F12)
        time.sleep(2)
        # 输入框中输入搜索内容并按下回车键
        query.send_keys('selenium')
        query.send_keys(Keys.ENTER)
        time.sleep(2)
    # 2019.2.27 add by linux超
    def testSimulationCombinationKeys(self):
        '''
        模拟组合按键
        :return:
        '''
        from selenium.webdriver import ActionChains
        from selenium.webdriver.common.keys import Keys
        import time
        url = 'http://www.baidu.com'
        self.driver.get(url)
        # 定位输入框
        input = self.driver.find_element_by_id('kw')
        input.send_keys('python')
        time.sleep(2)
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        time.sleep(2)
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
        time.sleep(1)
        self.driver.find_element_by_id('su').click()
    
    def testSimulationLeftClickMouseOfprocess(self):
        '''
        模拟鼠标左键按下与释放
        鼠标左键点击百度首页的新闻（新闻左键点击不放会变为蓝色）
        :return:
        '''
        from selenium.webdriver import ActionChains
        import time
        url = 'http://www.baidu.com'
        self.driver.get(url)
        element = self.driver.find_element_by_link_text('新闻')
        # 按下鼠标左键并保持
        ActionChains(self.driver).click_and_hold(element).perform()
        time.sleep(2)
        #释放鼠标左键
        ActionChains(self.driver).release(element).perform()
        time.sleep(2)
    def testMouseOnElement(self):
        '''
        鼠标悬停在某个元素上
        :return:
        '''
        from selenium.webdriver import ActionChains
        import time
        url = 'http://www.baidu.com'
        self.driver.get(url)
        newInfo = self.driver.find_element_by_link_text('新闻')
        hao123 = self.driver.find_element_by_link_text('hao123')
        action = ActionChains(self.driver)
        action.move_to_element(newInfo).perform()
        time.sleep(2)
        action.move_to_element(hao123).perform()
    #判断元素是否存在
    def isElementpresent(self,*element):
        from selenium.common.exceptions import NoSuchElementException
        try:
            self.driver.find_element(*element)
        except NoSuchElementException as e:
            print(e)
            return False
        else:
            return True
    def testIselementPresent(self):
        url = 'http://www.sogou.com'
        element = ('id', 'query')
        self.driver.get(url)
        ret = self.isElementpresent(*element)
        if ret is True:
            print('元素存在')
        else:
            print('元素不存在')
    #通过title属性识别和操作新弹出窗口的浏览器窗口
    def testTitleWindow(self):
        from selenium.common.exceptions import NoSuchElementException, TimeoutException
        import time
        url = 'file:///C:/Users/v-xug/Desktop/titleWindow.html'
        self.driver.get(url)
        sogou = self.driver.find_element_by_link_text('sogou 搜索')
        sogou.click()
        time.sleep(3)
        # 获取所有的窗口句柄
        all_handles = self.driver.window_handles
        # 打印当前窗口的句柄
        # print(self.driver.current_window_handle)
        print(len(all_handles))
        if len(all_handles) > 0:
            try:
                # 遍历每一个窗口
                for windowhandl in all_handles:
                    self.driver.switch_to.window(windowhandl)
                    # 每一个窗口的标题
                    print('窗口',self.driver.title)
                    if self.driver.title == '搜狗搜索引擎 - 上网从搜狗开始':
                        inputBox = self.driver.find_element_by_id('query')
                        inputBox.send_keys('python')
                    time.sleep(2)
            except NoSuchElementException as e:
                print(e)
            except TimeoutException as e:
                print(e)
        self.driver.switch_to.window(all_handles[0])
        print(self.driver.title)
        self.assertEqual(self.driver.title, '使用title属性识别和操作新弹出的浏览器窗口')
    def testHandleFrame(self):
        '''
        操作frame中的页面元素
        :return:
        '''
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.common.exceptions import TimeoutException

        self.driver.get(r'file:///C:/Users/v-xug/Desktop/frameset.html')
        self.driver.switch_to.frame(0) # 切换到第一个frame中
        left_ele_text = self.driver.find_element_by_xpath('//p')
        leftText = left_ele_text.text
        self.assertEqual(leftText, '这是左侧frame页面上的文字')
        button = self.driver.find_element_by_tag_name('input')
        button.click()
        try:
            alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            print(alert.text)
            alert.accept()
        except TimeoutException as e:
            print(e)
        self.driver.switch_to.default_content() # 跳到默认的frame
        self.driver.switch_to.frame(1) # 跳到第二个frame中
        middle_ele = self.driver.find_element_by_xpath('//p')
        print(middle_ele.text)
        middle_input = self.driver.find_element_by_tag_name('input')
        middle_input.send_keys('python')
        self.assertEqual(middle_ele.text, '这是中间frame页面上的文字')

        self.driver.switch_to.default_content()

    def testHandleCookie(self):
        '''
        操作页面的cookie信息
        :return:
        '''
        self.driver.get('https://www.sogou.com/')
        # 获取当前页面的所有cookie信息
        cookies = self.driver.get_cookies()
        for cookie in cookies:
            print('%s->%s->%s->%s->%s'%(cookie['domain'],cookie['name'], cookie['value'],cookie['expiry'],cookie['path']))
        # 获取name为suv的cookie信息
        ck = self.driver.get_cookie('SUV')
        print('%s->%s->%s->%s->%s' % (
        ck['domain'], ck['name'], ck['value'], ck['expiry'], ck['path']))

        # 删除name为abtest的cookie信息
        print(self.driver.delete_cookie('ABTEST'))
        # 删除所有的cookie信息
        self.driver.delete_all_cookies()
        print(self.driver.get_cookies())

        # 添加自定义cookie信息
        self.driver.add_cookie({'name':'gloryroadTrain','value':'1479697159269020'})
        # 查看cookie信息
        print(self.driver.get_cookie('gloryroadTrain'))
    def testSetLoadPageTimeOut(self):
        '''
        指定页面加载时间
        :return:
        '''
        import time
        from selenium.common.exceptions import TimeoutException
        from selenium.webdriver.common.keys import Keys
        self.driver.set_page_load_timeout(10)
        try:
            starttime = time.time()
            self.driver.get('https://mail.126.com')
        except TimeoutException:
            print('页面加载超时')
            self.driver.execute_script('window.stop()')

        end = time.time() - starttime
        print(end)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//div[@id='loginDiv']/iframe"))
        time.sleep(2)
        username = self.driver.find_element_by_xpath("//input[@name='email']")
        username.send_keys('281754043')
        time.sleep(2)
        password = self.driver.find_element_by_xpath("//input[@name='password']")
        password.send_keys('xiaochao11520')
        password.send_keys(Keys.ENTER)
    """
    def test_AjaxBykeys(self):
        '''
        在ajax方式产生的悬浮框中，单击选择包含某个关键字的选项
        :return:
        '''
        from selenium.webdriver.common.keys import Keys
        import time

        self.driver.get('https://www.sogou.com')
        query = self.driver.find_element_by_xpath("//input[@id='query']")
        query.send_keys('python')
        time.sleep(2)
        # 向下选择第三个选项
        for i in range(3):
            query.send_keys(Keys.DOWN)
            time.sleep(1)
        query.send_keys(Keys.ENTER)
    def tearDown(self):
        # self.driver.quit()
        pass


if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(MyTest('testMultipleOptions'))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    unittest.main()
