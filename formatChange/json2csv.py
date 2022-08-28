# coding:utf-8

import pandas as pd

__author__ = 'SongGuoRong'

if __name__ == "__main__":
    # 将json格式转换成csv格式
    pd.read_json("demo.json").to_csv("demo_result.csv")
    print("done!")
