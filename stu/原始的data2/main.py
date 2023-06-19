from util.riskUtil import riskUtil
import pandas as pd
import swifter
import vaex


if __name__ == '__main__':
    pd.set_option('display.max_rows', 500)       # 显示行数
    pd.set_option('display.max_columns', 500)    # 显示列数
    pd.set_option('display.width', 1000)         # 显示宽度
    data1 = pd.read_csv("data1.csv", encoding="utf-8")      # 包含性别数据
    data2 = pd.read_csv("data2.csv", encoding="utf-8")

    # 数据匹配，匹配到性别数据
    # 数据去重
    data1.drop_duplicates(['校园卡号'], keep='first', inplace=True)
    data2 = data2.merge(data1[['校园卡号', '性别']], on='校园卡号')
    # data2 = data2.merge(data1[['校园卡号', '性别']], on='校园卡号', validate='one_to_one')
    data2['校园卡号'] = data2['校园卡号'].map(lambda x: str(x)) + '-' + data2['性别']

    # 数据处理
    df = data2
    # apply函数特别慢 axis=1行操作
    df['消费时间'] = df['消费时间'].swifter.apply(riskUtil.timeFormat)
    df['tsm'] = df['消费时间'].swifter.apply(riskUtil.Time2Str)

    # 数据裂变，一行变两行 (level=-1表示最后一个索引)reset_index表示重置为数字索引
    df = df.set_index(["校园卡号", "消费时间", '消费地点'])["tsm"].str.split(";", expand=True).stack().reset_index(drop=True, level=-1).reset_index().rename(columns={0: "tsm"})

    # 匹配构图
    merge = pd.merge(df, df, on=['tsm', '消费地点'], how='inner')
    # 排除
    df_1 = merge[merge['校园卡号_x'] != merge['校园卡号_y']]
    # 时间作差，大于5分钟搞得排除
    df_1['diff'] = (pd.to_datetime(df_1['消费时间_x']) - pd.to_datetime(df_1['消费时间_y'])).dt.seconds / 60
    df_1 = df_1[df_1['diff'] <= 5]

    # 提取小时，按共同出现的小时计数
    df_1['date'] = df_1['tsm'].apply(lambda x: x[0:10])

    # 统计两两关联的次数，这里比较简单，不按天，也不计算相似度了(这里超级慢需要优化) swifter不支持 groupby 加速
    # df_2 = df_1.groupby(['校园卡号_x', '校园卡号_y']).agg({'date': pd.Series.nunique}).reset_index()
    # 使用vaex加速计算
    df_2 = df_1.groupby(by=['校园卡号_x', '校园卡号_y'], sort=False).apply(lambda x: pd.Series({'date': x['date'].nunique()})).reset_index()
    df_vaex = vaex.from_pandas(df_1)
    groupby = df_vaex.groupby(by=['校园卡号_x', '校园卡号_y'], agg={'date': vaex.agg.nunique})


    # 降序排列
    df_2 = df_2.sort_values(by='date', ascending=False)

    # 阈值确定
    # 给关系加阈值，大于20次的算是比较强的关联了
    df_3 = df_2[df_2['date'] >= 20]

    # LPA算法分群
    print("test")










