---
description: LaTeX
---

# LaTex

原文地址：https://www.jianshu.com/p/a0aa94ef8ab2

## 1. 呈现位置
* 行内显示：`$...$`  
  这是行内：$\sum_{i=0}^N\int_{a}^{b}g(t,i)\text{d}t$
* 单独显示：`$$...$$`  
  这是单独一样：

  $$\sum_{i=0}^N\int_{a}^{b}g(t,i)\text{d}t$$

## 2. 希腊字母
| 显示 | 命令 | 显示 | 命令 |
| --- | --- | --- | --- |
| $\alpha$ | \alpha | $\beta$ | \beta |
| $\gamma$ | \gamma | $\delta$ | \delta |
| $\epsilon$ | \epsilon | $\zeta$ | \zeta |
| $\eta$ | \eta | $\theta$ | \theta |
| $\iota$ | \iota | $\kappa$ | \kappa |
| $\lambda$ | \lambda | $\mu$ | \mu |
| $\nu$ | \nu | $\xi$ | \xi |
| $\pi$ | \pi | $\rho$ | \rho |
| $\sigma$ | \sigma | $\tau$ | \tau |
| $\upsilon$ | \upsilon | $\phi$ | \phi|
| $\chi$ | \chi | $\psi$ | \psi |
| $\omega$ | \omega |  |  |

* 需要大写希腊字母，将命令首字母大写即可  
  \Gamma呈现为：$\Gamma$
* 需要斜体希腊字母，将命令前加上var前缀即可。  
  \varGamma呈现为：$\varGamma$  

## 3. 字母修饰

### 3.1 上下标

* 上标：^
* 下标：_

举例：C_n^2 呈现为$C_n^2$

### 3.2 矢量

\vec a 呈现为$\vec a$  
\overrightarrow{xy} 呈现为$\overrightarrow{xy}$

### 3.3 字体

* Typewriter: \mathtt{A}呈现为$\mathtt{A}$
    * $\mathtt{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$
* Blackboard Bold: \mathbb{A}呈现为$\mathbb{A}$
    * $\mathbb{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$
* Sans Serif: \mathsf{A}呈现为$\mathsf{A}$
    * $\mathsf{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$

### 3.4 分组

* 使用{}将具有相同等级的内容扩入其中，成组处理
* 举例：10^{10}呈现为$10^{10}$,而10^10呈现为$10^10$

### 3.5 括号

* 小括号：()呈现为$()$
* 中括号：[]呈现为$[]$
* 尖括号：\langle,\rangle呈现为$\langle,\rangle$
    * 此处为与分组符号{}相区别，使用转义字符\
* 使用\left(或\right)使符号大小与邻近的公式相适应；该语句适用于所有括号类型
    * (\frac{x}{y})呈现为$(\frac{x}{y})$
    * \left(\frac{x}{y}\right)呈现为$\left(\frac{x}{y}\right)$
    * [\frac{x}{y}]呈现为$[\frac{x}{y}]$
    * \left[\frac{x}{y}\right]呈现为$\left[\frac{x}{y}\right]$

### 3.6 求和、极限与积分

* 求和：\sum
    * 举例：\sum_{i=1}^n{a_i}呈现为$\sum_{i=1}^n{a_i}$
* 极限：\lim
    * 举例：\lim_{x\to 0}呈现为$\lim_{x\to0}$
* 积分：\int
    * 举例：\int_0^\infty{fxdx}呈现为$\int_0^\infty{fxdx}$

### 3.7 分式与根式

* 分式(fractions):\frac{公式1}{公式2}呈现为$\frac{公式1}{公式2}$
* 根式:\sqrt[x]{y}呈现为$\sqrt[x]{y}$

### 3.8 特殊函数

* \函数名
* 举例：\sin x,\ln x,\max(A,B,C)呈现为$\sin x,\ln x,\max(A,B,C)$

### 3.9 特殊符号

| 显示 | 命令 |
| --- | --- |
| $\infty$ | \infty |
| $\cup$ | \cup |
| $\cap$ | \cap |
| $\subset$ | \subset |
| $\subseteq$ | \subseteq |
| $\supset$ | \supset |
| $\in$ | \in |
| $\notin$ | \notin |
| $\varnothing$ | \varnothing |
| $\forall$ | \forall |
| $\exists$ | \exists |
| $\lnot$ | \lnot |
| $\nabla$ | \nabla |
| $\partial$ | \partial |

### 3.10 空格

* LaTeX语法本身会忽略空格的存在
* 小空格：a\ b 呈现为$a\ b$
* 4格空格：a\quad b 呈现为$a\quad b$

## 4. 矩阵
### 4.1 基本语法
起始标记`\begin{matrix}`，结束标记`\end{matrix}`  
每一行末尾标记`\\`，行间元素之间以`&`分隔  
举例:
```
$$\begin{matrix}
1&0&0\\
0&1&0\\
0&0&1\\
\end{matrix}$$
```
呈现为：

$$\begin{matrix}
1&0&0\\
0&1&0\\
0&0&1\\
\end{matrix}$$

### 4.2 矩阵边框
* 在起始、结束标记处用下列词替换`matrix`
* `pmatrix` ：小括号边框
* `bmatrix` ：中括号边框
* `Bmatrix` ：大括号边框
* `vmatrix` ：单竖线边框
* `Vmatrix` ：双竖线边框

### 4.3 省略元素
* 横省略号：\cdots
* 竖省略号：\vdots
* 斜省略号：\ddots  
举例
```
$$\begin{bmatrix}
{a_{11}}&{a_{12}}&{\cdots}&{a_{1n}}\\
{a_{21}}&{a_{22}}&{\cdots}&{a_{2n}}\\
{\vdots}&{\vdots}&{\ddots}&{\vdots}\\
{a_{m1}}&{a_{m2}}&{\cdots}&{a_{mn}}\\
\end{bmatrix}$$
```
呈现为：

$$\begin{bmatrix}
{a_{11}}&{a_{12}}&{\cdots}&{a_{1n}}\\
{a_{21}}&{a_{22}}&{\cdots}&{a_{2n}}\\
{\vdots}&{\vdots}&{\ddots}&{\vdots}\\
{a_{m1}}&{a_{m2}}&{\cdots}&{a_{mn}}\\
\end{bmatrix}$$

### 4.4 阵列
* 需要array环境：起始、结束处以{array}声明
* 对齐方式：在{array}后以{}逐列统一声明
    * 左对齐：`l`；剧中：`c`；右对齐：`r`
    * 竖直线：在声明对齐方式时，插入`|`建立竖直线
* 插入水平线：`\hline`

举例：
```
$$\begin{array}{c|lll}
{↓}&{a}&{b}&{c}\\
\hline
{R_1}&{c}&{b}&{a}\\
{R_2}&{b}&{c}&{c}\\
\end{array}$$
```
呈现为：

$$\begin{array}{c|lcl}
{↓}&{aaa}&{bbbb}&{cccc}\\
\hline
{R_1}&{c}&{b}&{a}\\
{R_2}&{b}&{c}&{c}\\
\end{array}$$

### 4.5 方程组
* 需要cases环境：起始、结束处以{cases}声明

举例
```
$$\begin{cases}
a_1x+b_1y+c_1z=d_1\\
a_2x+b_2y+c_2z=d_2\\
a_3x+b_3y+c_3z=d_3\\
\end{cases}
$$
```
呈现为：

$$\begin{cases}
a_1x+b_1y+c_1z=d_1\\
a_2x+b_2y+c_2z=d_2\\
a_3x+b_3y+c_3z=d_3\\
\end{cases}
$$