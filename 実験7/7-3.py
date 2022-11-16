with open('hlm.txt','r',encoding='UTF-8') as f1:
    stream=f1.read()
    jby=stream.count('贾宝玉')
    jby+=stream.count('宝玉')
    ldy=stream.count('林黛玉')
    ldy+=stream.count('黛玉')

print("[贾宝玉+宝玉]出现了",jby,"次")
print("[林黛玉+黛玉]出现了",ldy,"次")