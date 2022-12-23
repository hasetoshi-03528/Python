import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

plt.rcParams['font.sans-serif']=['SimHei']  #设置中文字体
plt.figure(figsize=(6,10))

fp=open('Epoch.txt','r')
lines = fp.readlines()   #读取数据

x = np.array([i for i in range(1,51)])
loss = []
val_loss = []
acc = []
val_acc = []

for line in lines:
    line=line.strip('\n')        #去除换行符
    line=line.split('\t')         #按制表符分隔
    loss.append(float(line[0]))            #训练集损失值
    acc.append(float(line[1]))       #训练集准确率
    val_loss.append(float(line[2]))        #验证集损失值
    val_acc.append(float(line[3]))    #验证集准确率

y1 = np.array(acc)
y2 = np.array(val_acc)
y3 = np.array(loss)
y4 = np.array(val_loss)


ax = plt.subplot(2,1,1,title="训练集和验证集的准确率")
plt.xlabel('训练轮数')
plt.ylabel('准确率')
#plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(7))
plt.scatter(x,y1,color='c',label='训练集准确率') #训练集准确率
plt.plot(x,y2,color='r',label='验证集准确率')  #验证集准确率
plt.legend(loc='lower right')

plt.subplots_adjust(hspace=0.3) #调整间距

plt.subplot(2,1,2,title="训练集和验证集的损失值")
plt.xlabel('训练轮数')
plt.ylabel('损失值')
#plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(7))
plt.scatter(x,y3,color='b',label='训练集损失值')
plt.plot(x,y4,color='r',label='验证集损失值')
plt.legend(loc='upper right')

plt.show()
