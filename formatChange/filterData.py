# coding:utf-8

import pandas as pd
import numpy as np

__author__ = 'SongGuoRong'

if __name__ == "__main__":
    # 数据过滤
    # 查询结果 [memberId, tags]
    out = np.array(pd.read_csv("demo_result.csv").values[:, 1]).tolist()
    # 原始数据[memberId] 需提前去重 (如果包含序号项，则values[:, 0]--> values[:, 1])
    sourceData = np.array(pd.read_csv("sourceData.csv").values[:, 0]).tolist()
    res = []
    for item in sourceData:
        if item not in out:
            res.append(item)

    # 加上column标题
    pd.DataFrame({"memberId": res}).to_csv("不包含名单.csv")
    print("done!")
