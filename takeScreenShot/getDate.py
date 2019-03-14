from datetime import date, datetime


def currentDate():
    '''
    获取当前日期
    :return:
    '''
    return str(date.today())

def currentTime():
    '''
    获取当前时间
    :return:
    '''
    return str(datetime.now().strftime('%H_%M_%S'))


if __name__=='__main__':
    print(type(currentDate()))
    print(currentTime())