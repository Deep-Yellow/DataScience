### 题目描述

给定一张n个点m条边的带权无向图G，对于G的每一棵生成树，我们定义这棵生成树的权值为：它所包含的所有边的边权按三进制不进位加法相加所得的数。

现在请你求出图G中所有的生成树的权值和（将生成树的权值由三进制转为十进制，做正常的十进制进位加法）。输出答案对10^9 + 7取模后的值即可。

### 输入描述

```
第一行两个整数n,m表示点数与边数。点从1~n编号。
接下来m行每行三个整数a,b,c表示一条连接(a,b)的边权为c的无向边。
边权以十进制形式给出。

数据范围：
30%的数据(共六个点) : n= 5,6,7,8,9,10
50%的数据:n≤30
70%的数据:n≤40
100%的数据:n≤100,m≤n(n-1)/2,0≤c≤10^4,保证无重边无自环。
```
### 输出描述

```
仅一行一个整数表示答案。
```

### 测试样例
#### 样例1:输入-输出-解释

```
5 7
3 2 7400
4 1 1618
4 2 9110
4 3 4264
5 1 537
5 2 4240
5 3 655
```
```
262221
```