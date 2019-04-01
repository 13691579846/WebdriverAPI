import win32clipboard as w
import win32con

class ClipBoard(object):

    @staticmethod
    def setText(value): # 设计剪切板的内容
        try:
            # 打开剪切板
            w.OpenClipboard()
            # 清空剪切版
            w.EmptyClipboard()
            # 写入数据
            w.SetClipboardData(win32con.CF_UNICODETEXT, value)
            # 关闭剪切版
            w.CloseClipboard()
        except Exception as e:
            raise e

    @staticmethod
    def getText(): # 获取剪切板的内容
        try:
            # 打开剪切板
            w.OpenClipboard()
            value = w.GetClipboardData()
            w.CloseClipboard()
        except Exception as e:
            raise e
        else:
            return value

if __name__=='__main__':
    ClipBoard.setText('python')
    value = ClipBoard.getText()
    print(value)