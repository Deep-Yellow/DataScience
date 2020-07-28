from FinalProject.codeSimVer1.analyse import code_sim

import os



mPath = "..\\codeSimFileAll"
a = os.listdir(mPath)
print(a)
for i in (0, 1, 2, 4, 6, 10, 12):
    root = mPath + '\\' + a[i]
    try:
        result = code_sim(i, root, 1)
        print(result)
    except BaseException as e:
        print(e)





