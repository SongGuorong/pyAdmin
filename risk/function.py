import datetime


def st_pt(x):
    """
    时间格式化
    """
    return str(datetime.datetime.strptime(x, "%Y/%m/%d %H:%M"))


if __name__ == '__main__':
    x = "2019-04-20 20:17"
    pt = st_pt(x)
    print(pt)
