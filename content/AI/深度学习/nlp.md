在多年的实验中，人们发现了认知的两个重要机制：一个是抽象，另一个是迭代。从原始信号，做低层抽象，逐渐向高层抽象迭代，在迭代中抽象出更高层的模式。这是认知的生物学原理。目前来看，深度学习在解决机器视觉和语音识别方面都获得了非常好的效果，相关的技术都已经商业化。所以，人们评价，通过深度学习理论及算法，人类终于找到了如何处理“抽象概念”这个亘古难题的方法。


* 词法分析
    1. 分词技术
    2. 词性标注
    3. 命名实体识别
    4. 语义消歧
* 句法分析
* 语义分析

| 词性 | 符号 |
| :--- | :--- |
| 形容词 | a |
| 名词 | n |
| 副词 | d |
| 人称代词 | rr |
| 动词 | v |


NLPIR-ICTCLAS汉语分词系统：http://ictclas.nlpir.org/

计算所汉语词性标记集：http://ictclas.nlpir.org/nlpir/html/readme.htm

命名实体识别2大步骤：
1. 实体边界识别
2. 确定实体类别
    1. 英文实体
    2. 中文实体


如何进行命名实体识别：
* 基于规则和词典的方法
* 基于统计的方法
    1. 隐马尔科夫模型（HiddenMarkovMode,HMM）
    2. 最大熵（MaxminumEntropy,ME）
    3. 支持向量机（Support VectorMachine,SVM）
    4. 条件随机场（ConditionalRandom Fields,CRF）



贝叶斯算法：

$$
P(c|x)=\frac{P(c)P(x|c)}{P(x)}=\frac{P(x,c)}{P(x)}
$$
朴素贝叶斯算法:贝叶斯算法 + 假定：给定目标值时属性之间相互条件独立

$$
P(c|x)=\frac{P(c)P(x|c)}{P(x)}=\frac{P(c)}{P(x)}\prod_{i=1}^{d}P(x_i|c)
$$

朴素贝叶斯算法常用情景：
1. 文本分类
2. 垃圾邮件过滤
3. 多分类实时预测
4. 拼写纠错

## 马尔科夫过程
* 马尔科夫过程（markov process）是一类随机过程
* 在已知目前状态（现在）的条件下，他未来的演变(将来)不依赖于他以往的演变（过去）。主要研究一个系统的状况及其转移的理论。他是通过对不同状态的初始概率以及状态之间的转移概率的研究，来确定状态的变化趋势，从而达到对预测未来的目的
* 马尔科夫链（markov chain）是指具有马尔科夫性质的离散事件随机过程,即状态和状态参数都是离散的马尔科夫过程，是最简单的马尔科夫过程

## 隐马尔科夫模型
* 隐马尔科夫模型是马尔科夫链的一种，他的状态不能直接观察到，但能通过观测向量序列观察到，每个观测向量都是通过某些概率密度分布表现为各种状态，每一个观测向量是由一个具有相应概率密度分布的状态序列产生

## 语料库的种类
* 异质的
* 同质的
* 系统的
* 专用的

## 语聊的获取途径
* 开放性语料数据集
    * 中科院自动化所的中英文新闻语料库
    * 搜狗的中文新闻语料库
    * 人工生成的机器阅读理解数据集（微软）
    * 一个开放问题与回答的挑战数据集（ 微软）
* 爬虫技术
* 自有平台

## 语料的处理
* 获取语料
* 格式化文本
* 特征工程

## nlp中的语言模型
* Unigram models(一元文法统计模型)
* N-gram 语言模型(N元模型)

都属于概率语言模型

## 概率语言模型
* 预测字符串概率
* 动机
* 如何计算

## 一元文法统计模型
$$
p(s)=p(w1)*p(w2)*p(w3)*\cdots*p(wn)\\
p(我喝水)=p(我)*p(喝)*p(水)
$$
## 二元文法统计模型
$$
p(s)=p(w1|<s>)*p(w2|w1)*p(w3|w2)*\cdots*p(</s>|wn)\\
p(<s>我喝水</s>)=p(我|<s>)*p(喝|我)*p(水|喝)*p(</s>|水)
$$

二元模型比一元模型能更好地get到两个词语之间的关系信息

N元模型N越大越好吗？
N大于3时基本就无法处理了,参数空间太大。另外它不能表示词与词之间的关联性（当前词与很远的词没啥关系了）

## 文本处理方法
* 数据清洗（去掉无意义的标签、url和符号等）
* 分词、大小写转换、添加句首句尾、词性标注
* 统计词频、抽取文本特征、特征选择、计算特征权重、归一化
* 划分训练集和测试集









分词方法如下：
基于词典的匹配:前向最大匹配、后向最大匹配。
基于字的标注:最大熵模型、条件随机场模型、感知器模型。 
其他方法:与词性标注结合、与句法分析结合。

词性标注方法：
概率方法、隐马尔可夫模型的词性标注方法、机器学习规则的方法等。

文本分类常用算法：
决策树、朴素贝叶斯、神经网络、支持向量机、线性最小平方拟合、KNN、遗传算法、最大熵等，广泛应用于垃圾过滤、新闻分类、词性标注等。

典型的文本挖掘方法包括文本分类、文本聚类、信息抽取、概念/实体挖掘、情感分析和观点分析等。

信息抽取：
简单可以理解为从给定文本中抽取重要的信息，比如时间、地点、人物、事件、原因、 结果、数字、日期、货币、专有名词等。通俗说来，就是要了解谁在什么时候、什么原因、 对谁、做了什么事、有什么结果，涉及实体识别、时间抽取、因果关系抽取等关键技术。

问答系统使用了大量有别于传 统资讯检索系统的自然语言处理技术，如自然语言剖析(Natural Language Parsing)、问题分 类(Question Classification)、专名辨识(Named Entity Recognition)等。

一般而言，大众使用机器翻译的目的只是为了获知原文句子或段落的要旨，而不是精确 的翻译。总的来说，机器翻译的效果并没有达到可以取代人工翻译的程度，所以目前还无法 成为正式的翻译。