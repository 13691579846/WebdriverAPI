from takeScreenShot.getDate import currentTime, currentDate
import os

# 生成日期+时间的目录
def createDir():
    currentDir = os.path.dirname(os.path.abspath(__file__))
    dateDir = os.path.join(currentDir, currentDate())
    if not os.path.exists(dateDir):
        os.mkdir(dateDir)
    timeDir = os.path.join(dateDir, currentTime())
    if not os.path.exists(timeDir):
        os.mkdir(timeDir)
    return timeDir
if __name__ == '__main__':
    timeDir = createDir()
    print(timeDir)