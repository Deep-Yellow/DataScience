# 实验报告——关于python题目分类 



#### 小组信息：3人 

181250093 柳斯宁 1225747052@qq.com 175 分工：代码下载和解压、分析代码难度部分



#### 研究问题：

题目分类，通过学生提交的代码源码和成绩信息，将不同的题目的代码进行分类，目的在于重建产生我们所感知到的模式的内在模型，连续的学习以使得对同一知识点的理解更加深刻。

#### 代码开源地址：<https://github.com/NJU-SE-LHCL/DataScience>

#### 代码结构

![image-20200726112331410](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20200726112331410.png)

其中

analyseDifficulty 部分是分析以代码难度进行分类

codeSim 部分是分析代码相似度 docAndPPT 用来放PPT

testfile 和testfiles是sample.json下载的代码  代码文件夹是test_data下载的代码 

准备文件夹里是下载和解压同学代码的代码

#### 研究方法

数据集：从云端下载的学生代码main.py和标准答案answer.py 以及test_data.json中学生答题情况

数据分析方法：通过计算数据的数学期望获得变量平均取值的大小，计算偏度即数据的三阶标准化矩计算呈正态分布的数据的整体分布特点 

#### 具体案例分析（研究方法的具体说明）

代码下载（准备工作)：

![](https://nju-sjim.oss-cn-beijing.aliyuncs.com/DataScience/%E6%89%B9%E6%B3%A8%202020-06-03%20231511.png)

其中unzip.py负责实现代码的下载和解压，extractFile负责将可执行文件复制到可执行位置

![image-20200726160111255](https://nju-sjim.oss-cn-beijing.aliyuncs.com/DataScience/image-20200726160111255.png)

1. 代码按难度分类部分

##### analyseCodeToGenerateData.py 

读入所有同学的代码进行分析计算产生关于代码长度、提交成绩、运行时间的json数据用于进行分析

其中定义code类，将所有代码转化为code对象

![](https://nju-sjim.oss-cn-beijing.aliyuncs.com/DataScience/image-20200726161252367.png)

以每行代码的长度总和作为代码长度

![](https://nju-sjim.oss-cn-beijing.aliyuncs.com/DataScience/image-20200726161927007.png)

通过process.Popen方法运行所有题目并将所有cases作为输入计算每次运行时间求数学期望作为该代码运行时间的平均值

![](https://nju-sjim.oss-cn-beijing.aliyuncs.com/DataScience/image-20200726162315153.png)

将相同case_id的代码的长度、成绩、运行时间分别成表，并且分别求数学期望后成表,最后将所有列表生成Json文件

![](https://nju-sjim.oss-cn-beijing.aliyuncs.com/DataScience/image-20200726162626385.png)

##### fromDataToGraph.py 

用于数据可视化，将长度、成绩、运行时间分别生成图像，并且分析其偏度作为难度的影响因素，如果偏度为正证明该因素对难度有正影响，若为负则为负影响，最终通过各个影响因素的加权平均计算某case_id的难度（取值范围为0~100）

借助pandas库中的skew函数求的数据的偏度

![](https://nju-sjim.oss-cn-beijing.aliyuncs.com/DataScience/image-20200726170320918.png)

关各个因素对最终的难度影响因为不知道最终的成绩无法利用多元线性回归分析只好单独分析各自数据来进行估计。

最终成果图借助pyecharts API 将list数据转化为html数据图

![](https://nju-sjim.oss-cn-beijing.aliyuncs.com/DataScience/image-20200726171036468.png)

![](https://nju-sjim.oss-cn-beijing.aliyuncs.com/DataScience/image-20200726171152790.png)

代码长度方面显而易见难度大的题目代码长度差距显著，而相对简单的代码长度差距不明显，因此长度因素的权重可以相对较大

![](https://nju-sjim.oss-cn-beijing.aliyuncs.com/DataScience/image-20200726171844771.png)

代码平均成绩方面：未达到满分成绩对最终成绩的正影响较大，而满分成绩也并不一定说明题目足够简单，相对来说对最终题目难度影响较小，因此权重适中

![](https://nju-sjim.oss-cn-beijing.aliyuncs.com/DataScience/image-20200726172331043.png)

代码运行时间方面：因为代码运行时间与计算机状态有关随机性相对较大，因此权重较低

其中为了说明代码运行时间和代码长度之间并没有直接的线性关系将二者数据进行了比较分析

![](https://nju-sjim.oss-cn-beijing.aliyuncs.com/DataScience/image-20200726172954667.png)

显而易见二者并没有明显的线性关系，说明采用加权平均的分析方法具有可行性

求最终的难度时，将影响因素中最大最小数据差值作为span,各个影响因素数值与该因素数值最小值的查占span的比值乘100以进行数值标准化，再乘以各影响因素的权重得出最终的难度值，其中偏度影响因素按照正负对最终成绩进行正负影响

![](https://nju-sjim.oss-cn-beijing.aliyuncs.com/DataScience/image-20200726165812715.png)



最终成果如下：

![](https://nju-sjim.oss-cn-beijing.aliyuncs.com/DataScience/image-20200726173529557.png)

2. 题目种类分类

#### 对老师说的话

