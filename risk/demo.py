import warnings

from LPA.lpa import LPA
import networkx as nx
from networkx.algorithms.community import asyn_lpa_communities as lpa
import matplotlib.pyplot as plt

if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    G = nx.karate_club_graph()
    com = list(lpa(G, weight='weight'))    # com显示了社区的节点，这里的话，可以根据社区的大小进行排序然后设置阈值
    print('社区', com)
    print('社区数量', len(com))

    # 画图
    pos = nx.spring_layout(G)
    NodeId = list(G.nodes())
    node_size = [G.degree(i) ** 1.2 * 90 for i in NodeId]  # 节点大小

    plt.figure(figsize=(8, 6))  # 设置图片大小
    nx.draw(G, pos, with_labels=True, node_size=node_size, node_color='w', node_shape='.')

    color_list = ['pink', 'orange', 'r', 'g', 'b', 'y', 'm', 'gray', 'black', 'c', 'brown']

    for i in range(len(com)):
        nx.draw_networkx_nodes(G, pos, nodelist=com[i], node_color=color_list[i+2], label=True)

    plt.show()


# if __name__ == '__main__':
#     # run lpa
#     G = nx.karate_club_graph()  # 空手道数据集
#
#     # 给节点添加标签
#     for node in G:
#         # 用labels的状态
#         G.add_node(node, labels=node)
#
#     LPA.lpa(G)
#     com = set([G.nodes[node]['labels'] for node in G])
#     print("社区数量", len(com))
#     LPA.draw_picture(G)
