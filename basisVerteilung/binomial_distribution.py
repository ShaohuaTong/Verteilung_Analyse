import math

import numpy as np
from matplotlib import pyplot as plt
from scipy import stats

def count(lis):
    lis = np.array(lis)
    key = np.unique(lis)
    x = []
    y = []
    for k in key:
        mask = (lis == k)
        list_new = lis[mask]
        v = list_new.size
        x.append(k)
        y.append(v)
    return x, y

def binomial(n, p):
    result = np.random.binomial(n, p, 10000)  # 得到采样结果
    a, b = count(result)

    # 绘制结果分布图
    fig = plt.figure(num=1, figsize=(15, 8), dpi=80)
    plt.subplot(2, 2, 1)
    plt.bar(a, height=b, width=0.5, color='lightskyblue', edgecolor='white')
    plt.title('Ergebnisverteilung', fontsize=15)
    plt.ylim(top=10000)
    plt.xlim(right=n)
    x_ticks = np.arange(0, n + 1, 1)
    plt.xticks(x_ticks)
    plt.xlabel('number')
    plt.ylabel('counter')

    # 绘制pmf柱状图
    plt.subplot(2, 2, 2)
    plt.hist(result, bins=x_ticks, align='left', density=True, rwidth=0.5)  # 绘制直方图
    plt.title('PMFverteilung', fontsize=15)
    plt.xticks(x_ticks)
    plt.xlabel('number')
    plt.ylabel('probability')

    k = np.arange(0, n)
    binomial = stats.binom.pmf(k, n, p)

    plt.subplot(2, 2, 3)
    plt.plot(k, binomial, 'ro-')
    plt.xlabel('number')
    plt.ylabel('probalility')

    k1 = (n + 1) * p
    k2 = (n + 1) * p - 1
    k3 = math.floor(k1)

    if k3 == k1:
        plt.text((n + 1) * p, n * p, 'Wenn k = %d oder %d ist, wird der Maximalwert erhalten.' % (k2, k1),
                 color='mediumvioletred')
    else:
        plt.text((n + 1) * p, n * p, 'Wenn k = %d ist, wird der Maximalwert erhalten. ' % k3,
                 color='mediumvioletred')

    # plt.savefig('aa.png', dpi=1600, bbox_inches='tight')
    # plt.show()
    return fig
