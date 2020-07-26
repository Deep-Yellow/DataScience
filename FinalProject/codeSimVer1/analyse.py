
import ast
import os
import json

from zss import Node, simple_distance


def get_dtc_tree(node):
    distance_node = Node(type(node).__name__)
    tree_size = _dfs(node, distance_node)
    return distance_node, tree_size

def _tree_edit_distance(distance_node1,tree_size1, node2):
    distance_node2, tree_size2 = get_dtc_tree(node2)
    distance = simple_distance(distance_node1, distance_node2)
    return 1 - 1.0 * distance / max(tree_size1, tree_size2)


def _dfs(root, dtc_node=None):
    _tree_size = 0
    nodes = ast.iter_child_nodes(root)
    for _node in nodes:
        if type(root).__name__ == 'Load':
            continue
        _tree_size += 1
        if dtc_node is not None:
            _dtc_node = Node(type(_node).__name__)
            dtc_node.addkid(_dtc_node)
        else:
            _dtc_node = None
        _tree_size += _dfs(_node, _dtc_node)
    return _tree_size

class _CodeSim:

    def __init__(self, id,fileRoot, beginIndex):

        self.id = id
        self.root = fileRoot
        self.dirList = os.listdir(fileRoot)
        self.begin = beginIndex
        self.file1Path = fileRoot + '\\' + self.dirList[beginIndex] + '\\' + 'main.py'
        self.length = len(self.dirList)

        # 得到比较主体的Node
        with open(self.file1Path, encoding="utf-8") as f:
            self._code1 = f.read()
        self.node1= ast.parse(self._code1)
        self.distance_node1, self.tree_size1 = get_dtc_tree(self.node1)

    @property
    def tree_edit_distance(self):
        simResult=[]
        for i in range(self.begin+1,self.length):
            file2Path = self.root+ '\\'+ self.dirList[i]+ '\\'+ 'main.py'
            with open(file2Path, encoding="utf-8") as f:
                code2 = f.read()
            try:
                node2 = ast.parse(code2)
                s = _tree_edit_distance(self.distance_node1,self.tree_size1, node2)
                print('#',self.id,'NO.',self.begin,"similarity with NO.",i,'is',s)
                simResult.append(s)
            except BaseException as e:
                print(e)
                simResult.append(0.2)
        return simResult


def code_sim(id,fileroot,beginindex):
    # fileroot 谁的文件夹 beginindex 从哪个开始
    list1 = _CodeSim(id,fileroot,beginindex).tree_edit_distance



    Filename = 'Stu'+str(id)+'--'+str(beginindex)+'.json'
    try:
        with open(Filename, 'w', encoding='utf-8') as fs:
            json.dump(list1, fs)

    except IOError as e:
        print(e)
        return('Stu '+str(id)+'----'+str(beginindex)+'写入失败')

    return ('Stu '+str(id)+'----'+str(beginindex)+' finished')