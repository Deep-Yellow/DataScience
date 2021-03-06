
from queue import Queue

class TreeNode:
    lch = None
    rch = None
    element = None

    def __init__(self, element, lch, rch):
        self.element = element
        self.lch = lch
        self.rch = rch


class Tree:
    root = None

    def __init__(self):
        self.root = None

    def maketree(self, data, left, right):
        if left != None and right != None:
            self.root = TreeNode(data, left, right)
        elif left == None and right != None:
            self.root = TreeNode(data, None, right)
        elif left != None and right == None:
            self.root = TreeNode(data, left, None)
        else:
            self.root = TreeNode(data, None, None)

    '''
   返货该节点处的高度，叶节点是0
    '''

    def getHeight(self):
        if self.root.lch == None and self.root.rch == None:
            return 0
        elif self.root.lch != None and self.root.rch == None:
            return 1 + self.root.lch.getHeight()
        elif self.root.lch == None and self.root.rch != None:
            return 1 + self.root.rch.getHeight()
        else:
            return 1 + max(self.root.lch.getHeight(), self.root.rch.getHeight())

    def getElement(self):
        return self.root.element

    def distance(self,node):
        if self.root.element == node.root.element:
            return 0
        elif self.root.lch == None and self.root.rch != None:
            return 1+self.root.rch.distance(node)
        elif self.root.lch != None and self.root.rch == None:
            return 1+self.root.lch.distance(node)
        elif self.root.lch == None and self.root.rch == None:
            return -100
        else:
            return 1+max(self.root.lch.distance(node),self.root.rch.distance(node))

    def isEmpty(self):
        if self.root == None:
            return True
        else:
            return False

    #广度优先搜索
    def BFS(self):
        result = []
        q=Queue()
        q.put(self)
        while q.empty() is not True:
            node = q.get()
            result.append(node)
            if node.root.lch:
                q.put(node.root.lch)
            if node.root.rch:
                q.put(node.root.rch)
        return result







line1 = input().split(" ")
n = int(line1[0])
root = line1[1]
node = []
# 开始建树
store = []
for i in range(n):
    line = input()
    store.append(line)
#确定node大小
Max = 0
for i in range(len(store)):
    if int(store[i].split(" ")[0])>Max:
        Max = int(store[i].split(" ")[0])
#初始化node
for i in range(Max+1):
    tree = Tree()
    node.append(tree)
for i in range(n):
    line = store[i].split(" ")
    element = line[0]
    leftch = int(line[1])
    rightch =int(line[2])
    if leftch!=0 and rightch != 0:
        node[int(element)].maketree(element,node[leftch],node[rightch])
    elif leftch == 0 and rightch !=0:
        node[int(element)].maketree(element, None, node[rightch])
    elif leftch != 0 and rightch ==0:
        node[int(element)].maketree(element,node[leftch],None)
    else:
        node[int(element)].maketree(element, None, None)

layers = []
BFS = node[int(root)].BFS()
for i in range(0,len(BFS)):
    distance = BFS[0].distance(BFS[i])
    if len(layers)<=distance:
        for j in range(distance-len(layers)+1):
            layers.append("")
    layers[distance]+=(BFS[i].getElement())
    layers[distance]+=" "
#第一阶段输出
for i in range(0,len(layers)):
    print("Level ",end="")
    print(i+1,end=" ")
    print(": ",end="")
    print(layers[i][:-1])
#第二阶段输出
for i in range(0,len(layers)):
    print("Level",end=" ")
    print(i+1,end=" ")
    print("from",end=" ")
    if i%2==0:
        print("left to right:",end=" ")
        print(layers[i][:-1])
    else:
        print("right to left:",end=" ")
        temp = list(layers[i][:-1].split(" "))
        temp.reverse()
        print(" ".join(temp))

