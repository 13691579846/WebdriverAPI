import win32api
import win32con

class SimulateKeyboard(object):
    # 按键对应的键盘码
    VK_CODE = {
        'enter' : 0x0D,
        'ctrl' : 0x11,
        'v' : 0x56
    }
    @staticmethod
    def keyDown(key): # 按下键
        try:
            win32api.keybd_event(SimulateKeyboard.VK_CODE[key],0,0,0)
        except Exception as e:
            raise e

    @staticmethod
    def keyUp(key): # 抬起键
        try:
            win32api.keybd_event(SimulateKeyboard.VK_CODE[key], 0, win32con.KEYEVENTF_KEYUP, 0)
        except Exception as e:
            raise e

    @staticmethod
    def oneKey(key): # 模拟单个按键
        SimulateKeyboard.keyDown(key)
        SimulateKeyboard.keyUp(key)

    @staticmethod
    def twoKey(key1, key2): # 模拟组合按键
        SimulateKeyboard.keyDown(key1)
        SimulateKeyboard.keyDown(key2)

        SimulateKeyboard.keyUp(key1)
        SimulateKeyboard.keyUp(key2)

if __name__=='__main__':
    from selenium import webdriver

    driver = webdriver.Firefox()
    driver.get('http://www.baidu.com')
    SimulateKeyboard.twoKey('ctrl', 'v')
