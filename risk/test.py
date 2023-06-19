import datetime
import pandas as pd


def Time2Str(tsm):
    t1 = datetime.datetime.fromisoformat(tsm)
    t0 = t1 - datetime.timedelta(days=0, hours=1)
    t2 = t1 + datetime.timedelta(days=0, hours=1)
    str1 = t0.strftime("%Y%m%d") + '(' + str(t0.hour).rjust(2, '0') + '#' + str(t1.hour).rjust(2, '0') + ')'
    str2 = t1.strftime("%Y%m%d") + '(' + str(t1.hour).rjust(2, '0') + '#' + str(t2.hour).rjust(2, '0') + ')'
    return str1 + ";" + str2


if __name__ == "__main__":
    df = pd.DataFrame({
        'Buy': ['BUY_03', 'BUY_02', 'BUY_01', 'BUY_04', 'BUY_03', 'BUY_02', 'BUY_01', 'BUY_04'],
        'Times': ['2021-11-16 00:03:32', '2021-11-16 00:12:23', '2021-11-16 00:22:07', '2021-11-16 21:10:24', '2021-11-16 21:18:05', '2021-11-16 21:22:02', '2021-11-16 21:42:57', '2021-11-16 23:51:39'],
        'Seller': ['Y', 'Y', 'Y', 'E', 'E', 'E', 'E', 'Y']})
    # 时间离散化
    df['tsm'] = df['Times'].apply(Time2Str)

    print(df)



