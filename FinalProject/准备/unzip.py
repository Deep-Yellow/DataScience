import json
from urllib import request, parse
import os
from urllib.parse import quote
import zipfile


def mkdir(path):
    # 引入模块

    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False


# 下载文件

f = open('../test_data.json', encoding='utf-8')  # 都先用sample测试
res = f.read()
data = json.loads(res)


# for k, v in data.items():
#     # v包括usereid 和 cases
#
#     print("这是k:"+k)
#     for i in v['cases']:
#
#         if (i['final_score'] == 100):
#             print(i['case_id'])
#             for m in i['upload_records']:
#
#                 print (m['score'])
#         for key, value in i.items():
#             print(key, "=", value)

def whetherDown(list1):
    if (len(list1['cases']) < 200):
        return False
    for b in list1['cases']:
        if(b['final_score']<100):
            return False
    return True

list2=[]
for a in data.values():
    if(whetherDown(a)):
        print(a['user_id'],len(a['cases']))
        list2.append(a['user_id'])
        outer = "D:\dataScience\FinalProject\codeSimFileAll\\" + str(a["user_id"])
        mkdir(outer)
        for case in a['cases']:
            if case['final_score'] == 100:
                print(case['case_id'], case['case_type'])
                for uploadRec in case['upload_records']:
                    if (uploadRec['score'] == 100):
                        filename = outer + "\\" + parse.unquote(os.path.basename(uploadRec['code_url']))
                        a = uploadRec['code_url']
                        request.urlretrieve(a, filename)
                        break
    else:
        continue


# 将下载的文件解压


# outest = "D:\dataScience\FinalProject\codeSimFileAll\\"
# ids = os.listdir(outest)
# for id in ids:
#     print(id)
#     zips = os.listdir(outest+str(id))
#     for zip in zips:
#         print(outest+id+"\\"+zip)
#         print(os.getcwd())
#         z=zipfile.ZipFile(outest+"\\"+id+"\\"+zip, 'r')
#         os.makedirs(outest+"\\"+id+"\\"+zip[:-5])
#         z.extractall(path=outest+"\\"+id+"\\"+zip[:-5])
#         z.close()
#         os.remove(outest+"\\"+id+"\\"+zip)



outest = "D:\dataScience\FinalProject\codeSimFileAll\\"
ids = os.listdir(outest)
print(ids)
for id in ids:
    print(id)
    zips = os.listdir(outest+str(id))
    for zip in zips:
        files = os.listdir(outest+id+"\\"+zip)
        for file in files:
            print(outest + id + "\\" + zip+'\\'+file)
            z = zipfile.ZipFile(outest + id + "\\" + zip+'\\'+file, 'r')
            z.extractall(path=outest + id + "\\" + zip)
            z.close()
            os.remove(outest + id + "\\" + zip+'\\'+file)
