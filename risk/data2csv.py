import pandas as pd



if __name__ == '__main__':
    pd.set_option('display.max_columns', None)
    dataFrame = pd.read_csv("data4.csv", encoding="utf-8")
    dataFrame['校园卡号'] = dataFrame['校园卡号'].apply(lambda x: (str(x))[:-2])
    dropDate = dataFrame
    # index=False表示不添加数字索引列
    dropDate.to_csv(r'data2.csv', sep=',', header=True, index=False, encoding='utf-8')
    print("done")

