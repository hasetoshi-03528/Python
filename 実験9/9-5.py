import matplotlib.pyplot as plt
score = [0.1, 0.3, 0.3, 0.05, 0.2, 0.05]
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.title("支出比例")
labels = ['学习用品', '日常用品', '伙食费', '通讯费', '娱乐费', '其他开支']
explode = (0, 0, 0, 0, 0.2, 0)
plt.axis("equal")
plt.pie(score, labels=labels, autopct='%4.1f%%')
plt.legend(bbox_to_anchor=(1, 0.6))
plt.show()
