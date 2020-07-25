from FinalProject.codeSim.analyse import code_sim
import json
import os

# allData = []

presentRoot = mPath + '\\' + a[3]
b = os.listdir(presentRoot)
print(len(b))

# for i in range(0, 2):
#     simtest = []
#     for j in range(i + 1, len(b)):
#         s = code_sim(presentRoot + '\\' + b[i] + '\\' + 'main.py', presentRoot + '\\' + b[j] + '\\' + 'main.py')
#         simtest.append(s)
#
#     print(len(simtest))
#     allData.append(simtest)

# simtest = []
for i in range(0, len(b) - 1):
    print(code_sim(presentRoot + '\\' + b[i] + '\\' + 'main.py', presentRoot + '\\' + b[i + 1] + '\\' + 'main.py'))
    # simtest.append(s)

# print(len(simtest))
# allData.append(simtest)

for i in range(4, 7):
    presentRoot = mPath + '\\' + a[i]
    b = os.listdir(presentRoot)
    print(len(b))

    # for j in range(0, 2):
    #     simtest = allData[j]
    #     for k in range(j + 1, len(b)):
    #         s = code_sim(presentRoot + '\\' + b[j] + '\\' + 'main.py', presentRoot + '\\' + b[k] + '\\' + 'main.py')
    #         print('#', i, "NO.", j, "Similarity with NO.", k, 'is', s)
    #         simtest[k - 1 - j] = simtest[k - 1 - j] + s
    #     print(len(simtest))
    # allData[j] = simtest
    # simtest = allData[j]
    for j in range(0, len(b) - 1):
        print(code_sim(presentRoot + '\\' + b[j] + '\\' + 'main.py', presentRoot + '\\' + b[j + 1] + '\\' + 'main.py'))
        # print('#', i, "NO.", j, "Similarity with NO.", k, 'is', s)
        # simtest[k - 1 - j] = simtest[k - 1 - j] + s
    # print(len(simtest))
    # allData[j] = simtest

# print(allData)
