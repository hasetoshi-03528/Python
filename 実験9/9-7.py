f=open(r'.\epoch.txt',"w")
loss = history.history['loss'] #训练集的损失
acc= history.history['accuracy'] #训练集的准确率
val_loss = history.history['val_loss'] #验证集上的损失
val_acc = history.history['val_accuracy'] #验证集上的准确率
for i in range(len(acc)):
    f.write(str(loss[i]) + '\t')
    f.write(str(acc[i])+ '\t')
    f.write(str(val_loss[i])+ '\t')
    f.write(str(val_acc[i])+ '\t')
    f.write('\n')
f.close()