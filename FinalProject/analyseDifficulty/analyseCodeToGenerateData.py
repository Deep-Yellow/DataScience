import json
import os
import shutil
import subprocess
import time


def isPy(list):
    for i in list:
        if "namespace" in i or "include" in i:
            return False
    return True


def copyFile(fileName):
    # target =
    fileList = os.listdir(fileName)
    for i in fileList:
        source = fileName + "/" + i + "/.mooctest/answer.py"
        target = fileName + "/" + i + ".py"
        shutil.copy(source, target)


class code:
    caseId = 0
    clen = 0  # 代码长度
    # complex = 0  # 代码时间复杂度
    score = []  # 代码历次提交成绩
    times = 0  # 运行时间
    fileName = ''  # 文件名
    text = []  # 代码
    examp = []

    def __init__(self, id, fileName, score):
        self.caseId = id
        self.fileName = fileName
        file = open(self.fileName + "answ"
                                    "er.py", 'r', encoding="utf-8")
        self.text = []
        while 1:
            line = file.readline()
            if not line:
                break
            self.text.append(line)
        file.close()

        with open(filename + "testCases.json", "r") as cases:
            self.examp = json.load(cases)
        self.clen = self.getlen()
        # self.complex = self.getComplex()
        self.score = score
        self.times = self.getTimes()

    def getlen(self):  #
        res = 0
        for line in self.text:
            res = res + len(line)
        return res

    # def getComplex(self):
    #
    #     recycleComplex = 0
    #     recursiveComplex = 0
    #     for line in self.text:
    #         print(line)
    #     if recycleComplex>recursiveComplex:
    #         res = recycleComplex
    #     else:
    #         res = recursiveComplex
    #     return res
    #
    def getTimes(self):
        rootdir = self.fileName + 'tests'
        if not os.path.exists(rootdir):
            os.mkdir(rootdir)
            for i in range(len(self.examp)):
                with open(filename + "tests/test_" + str(i) + ".txt", 'w')as f:
                    f.write(self.examp[i]['input'])

        list = os.listdir(rootdir)
        timeList = []
        for i in range(len(list)):
            path = os.path.join(rootdir, list[i])
            if os.path.isfile(path):
                file = open(path, 'r')
                start = time.perf_counter()
                cmd = subprocess.Popen("python " + filename.replace("/.mooctest/", ".py"), stdin=file, shell=True)
                end = time.perf_counter()
                timeList.append(end - start)
        return sum(timeList) / len(timeList)


allCode = []
f = open('../sample_short.json', encoding='utf-8')  #
res = f.read()
data = json.loads(res)
for k, v in data.items():
    print("这是k:" + k)
    for i in v['cases']:
        filename = "../testfiles/" + k + "/" + i['case_zip'][57:-5] + '/.mooctest/'
        case_id = i['case_id']
        final_score = i['final_score']
        scores = []
        for item in i['upload_records']:
            scores.append(item['score'])
        code_x = code(case_id, filename, scores)
        allCode.append(code_x)

code_sortedById = {}  # 相同题号的代码的对象字典
for i in allCode:
    code_withSameId = code_sortedById.get(i.caseId)
    id = i.caseId
    if isPy(i.text):
        if code_withSameId is None:
            code_withSameId = [i]
        else:
            code_withSameId.append(i)
    code_sortedById[id] = code_withSameId

id_list = []
len_list = []
score_list = []
time_list = []
for i in code_sortedById:
    item = code_sortedById[i]
    id_list.append(i)
    len_list_t = []
    score_list_t = []
    time_list_t = []
    for k in item:
        len_list_t.append(k.clen)
        score_list_t.append(sum(k.score)/len(k.score))
        time_list_t.append(k.times)
    len_list.append(sum(len_list_t) / len(len_list_t))
    score_list.append(sum(score_list_t) / len(score_list_t))
    time_list.append(round(sum(time_list_t) / len(time_list_t),5))

# 把代码信息生成数据
try:
    with open('id.json', 'w', encoding='utf-8') as fs:
        json.dump(id_list, fs)
    with open('length.json', 'w', encoding='utf-8') as fs:
        json.dump(len_list, fs)
    with open('score.json', 'w', encoding='utf-8') as fs:
        json.dump(score_list, fs)
    with open('time.json', 'w', encoding='utf-8') as fs:
        json.dump(time_list, fs)
except IOError as e:
    print(e)
print('保存数据完成!')
