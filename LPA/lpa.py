import random
import matplotlib.pyplot as plt
import networkx as nx


class LPA(object):
    @staticmethod
    def lpa(G, max_iter_num=10):
        """
        lpa标签传播算法
        :param G: 网络数据
        :param max_iter_num: 最大迭代次数
        :return:
        """
        currentIter = 0    # 迭代次数
        while currentIter < max_iter_num:
            currentIter += 1
            print("迭代次数", currentIter)

            for node in G:
                count = {}    # 记录邻居节点及其标签
                for nbr in G.neighbors(node):          # node的邻居节点
                    label = G.nodes[nbr]['labels']
                    count[label] = count.setdefault(label, 0) + 1

                # 找到出现次数最多的标签
                count_items = sorted(count.items(), key=lambda x: -x[-1])
                best_labels = [k for k, v in count_items if v == count_items[0][1]]
                # 当多个标签最大技术值相同时随机选取一个标签
                label = random.sample(best_labels, 1)[0]  # 返回的是列表，所以需要[0]
                G.nodes[node]['labels'] = label  # 更新标签

    @staticmethod
    def draw_picture(G):
        # 画图
        node_color = [float(G.nodes[v]['labels']) for v in G]
        pos = nx.spring_layout(G)    # 节点的布局为spring型
        plt.figure(figsize=(8, 6))   # 图片大小
        nx.draw_networkx(G, pos=pos, node_color=node_color)
        plt.show()

