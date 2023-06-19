# 风控处理工具
import datetime
import pandas as pd


class riskUtil(object):
    @staticmethod
    def timeFormat(x: str) -> str:
        """
        时间格式调整
        :param x: '2019/4/20 20:17'
        :return: '2019-04-20 20:17:00'
        """
        return str(datetime.datetime.strptime(x, "%Y/%m/%d %H:%M"))

    @staticmethod
    def Time2Str(tsm: str) -> str:
        """
        时间窗口
        :param tsm: 时间戳 2019-04-20 20:17:00
        :return:
        """
        t0 = datetime.datetime.fromisoformat(tsm)
        t1 = t0 + datetime.timedelta(days=0, hours=5 / 60)
        str1 = t0.strftime("%Y%m%d%H") + '(' + str(round(int(t0.minute / 5))).rjust(2, '0') + ')'
        str2 = t1.strftime("%Y%m%d%H") + '(' + str(round(int(t1.minute / 5))).rjust(2, '0') + ')'
        return str1 + ';' + str2

    @staticmethod
    def timeDiff(tx, ty):
        """
        时间作差
        (pd.to_datetime(df_1['消费时间_x']) - pd.to_datetime(df_1['消费时间_y'])).dt.seconds / 60
        :return:
        """
        return pd.to_timedelta(pd.to_datetime(tx) - pd.to_datetime(ty)).seconds / 60

    @staticmethod
    def countUnique(df, field):
        """
        统计组中唯一值次数(应用joblib加速计算)
        :param df:
        :return:
        """
        df[field] = pd.Series.nunique(df[field])
        return df

