from FinalProject.codeSimVer1.analyse import code_sim

import os

#Test2 1.2.3的 1.2题 Test5 5.7.11.13的1题 Test6 5 7 11 13的2题


mPath = "..\\codeSimFileAll"
a = os.listdir(mPath)
print(a)
for i in (4, 6, 10, 12):
    root = mPath + '\\' + a[i]
    try:
        result = code_sim(i, root, 1)
        print(result)
    except BaseException as e:
        print(e)





