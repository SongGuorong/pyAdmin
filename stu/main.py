from util.riskUtil import riskUtil
import pandas as pd
import vaex
import datetime

if __name__ == '__main__':
    start_time = datetime.datetime.now()
    # pd.set_option('display.max_rows', 500)       # 显示行数
    # pd.set_option('display.max_columns', 500)    # 显示列数
    # pd.set_option('display.width', 1000)         # 显示宽度
    # data1 = pd.read_csv("data1.csv", encoding="utf-8")      # 包含性别数据
    # data2 = pd.read_csv("data2.csv", encoding="utf-8")
    #
    # # 数据匹配，匹配到性别数据
    # # 数据去重
    # data1.drop_duplicates(['校园卡号'], keep='first', inplace=True)
    # data2 = data2.merge(data1[['校园卡号', '性别']], on='校园卡号')
    # df = vaex.from_pandas(data2)
    # df['校园卡号'] = df.apply(lambda dx, dy: (str(dx) + '-' + dy), arguments=[df['校园卡号'], df['性别']])
    # # df['校园卡号'] = df['校园卡号'].apply(lambda x: str(x)) + '-' + df['性别']
    # # 数据处理
    # df['消费时间'] = df['消费时间'].apply(riskUtil.timeFormat)
    # df['tsm'] = df['消费时间'].apply(riskUtil.Time2Str)
    # print("数据处理结束")
    # df = df.to_pandas_df()
    #
    # # 数据裂变，一行变两行 (level=-1表示最后一个索引)reset_index表示重置为数字索引
    # df = df.set_index(["校园卡号", "消费时间", '消费地点'])["tsm"].str.split(";", expand=True).stack().reset_index(drop=True, level=-1).reset_index().rename(columns={0: "tsm"})
    #
    # # 匹配构图
    # merge_pd = pd.merge(df, df, on=['tsm', '消费地点'], how='inner')
    # print("保存初步计算结果")
    # merge_pd.to_csv(r'merge.csv', header=True, index=False, encoding='utf-8')

    # 使用vaex加速计算
    merge = vaex.from_csv("merge.csv", convert=True, chunk_size=100_000, encoding='utf-8', progress=True)
    print("HDF5数据加载完毕")
    # 排除
    df_1 = merge[merge['校园卡号_x'] != merge['校园卡号_y']]
    # 时间作差，大于5分钟搞得排除
    df_1['diff'] = df_1.apply(riskUtil.timeDiff, arguments=[df_1['消费时间_x'], df_1['消费时间_y']])
    df_1 = df_1[df_1['diff'] <= 5]
    # 提取小时，按共同出现的小时计数
    df_1['date'] = df_1['tsm'].apply(lambda x: x[0:10])
    # groupby计算
    print("groupby计算开始")
    df_2 = df_1.groupby(by=['校园卡号_x', '校园卡号_y'], agg=vaex.agg.nunique(df_1['date']), progress=True)
    # df_2 = df_1.groupby(by=['校园卡号_x', '校园卡号_y'], agg={'date': vaex.agg.nunique}, progress=True)
    # 降序排列
    df_2 = df_2.sort(by='date', ascending=False)
    # 阈值确定
    # 给关系加阈值，大于20次的算是比较强的关联了
    df_3 = df_2[df_2['date'] >= 20]

    # LPA算法分群
    print(df_3.head(6))
    end_time = datetime.datetime.now()
    print("耗时：{} 秒".format((end_time - start_time).total_seconds()))
