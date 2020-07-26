import json
from FinalProject.codeSimVer1.analyse import code_sim
import os

# f = open('AverageOfFirst.json', encoding='utf-8')
# res = f.read()
# data = json.loads(res)
# mPath = "..\\codeSimFileAll\\49405"
# b=os.listdir(mPath)
# print(b)
# r=[]
# for i in range(0,199):
#     if(data[i]>0.3):
#         r.append(data[i])
# print(r)

f = open('AverageOfFirst.json', encoding='utf-8')
res = f.read()
data = json.loads(res)
f = open('AverageOfSecond.json', encoding='utf-8')
res =f.read()
data2 = json.loads(res)
mPath = "..\\codeSimFileAll\\49405"
b=os.listdir(mPath)
r=[]
list1=[]
list2=[]
count=0

for i in range(0, 198):
    count+=abs(data[i+1]-data2[i])
    # if(data2[i]>0.3):
    #     r.append(b[i+2][:-13])
    #     list1.append(data2[i])
    #     list2.append(i)
        # list1.append(data[i])
        # list2.append(data2[i+1])
print(count/200)
# print(list2)
# print(data2.index(max(list1)))
# print(list2)

# 42 58 53 32 13
#保存数据
# try:
#     with open('AverageOfSecond.json', 'w', encoding='utf-8') as fs:
#         aa=json.dumps(total,ensure_ascii=False)
#         fs.write(aa)
#
# except IOError as e:
#     print(e)
#
# print('保存数据完成!')
# mPath = "..\\codeSimFileAll\\49405"
# b=os.listdir(mPath)
# print(b[97])