
# 穷举法
# 1、构造所有的排列  
'''
解空间上的一次深度搜索

global X ,Ci(i=0,1,...)
X=[x0,x1...] #解空间
Ci可扩展空间

def permute(i):
    if X is a valid permutation:   //检测是一个可行解
        process it
    else:  //扩展部分解
        for each x in Ci:
            X[i]=x  //扩展解
            Ci+1=Ci\{x}  //更新可扩展空间
            permute(i+1)  //递归调用
'''

#如实现123排列
def perm_v3(X,S,i,n):
    if i==n: #可行解
        print(X)  #输出解
    else:
        for e in S:
            X[i]=e  #扩展解
            S1=S-{e}  #更新可扩展空间
            perm_v3(X,S1,i+1,n)  #递归调用
def  test_perm_v3():
    X=[0]*3
    S={1,2,3}
    perm_v3(X,S,0,3)
test_perm_v3()








#二、 回溯法
'''
穷举法：枚举所有的可能,
回溯：系统的穷举法

在穷举法的基础上,在每次扩展解时
多加一步判断,是否可以扩展,是:扩展解X[X0,X1,...Xi-1]->X[X0,X1,...Xi]
                         否：回溯（减枝）

基本框架：
Gloabl X=(x0,x1...)可行解,Ck(k=0,1,...)可扩展空间
procedure backtrack(i):
    if X is a feasible solution:  //检测是一个可行解 
        process it
    
    Compute Ck  计算可扩展空间  (这里就相当于减枝了,不去扩展所有解,而是只扩展可行解)
    for each x in Ck:
        X[i]=x  //扩展解
        backtrack(i+1)  //递归调用

    '''

#例一、背包问题
'''
输入物品价值P=[p1,p2,...,pn],物品重量W=[w1,w2,...,wn],容量C
最大化问题: V=max{p1x1+p2x2+...+pnxn} (xi=0,1)

如:物品价值P=[10,6,5],物品重量W=[5,4,3],容量C=8
''' 
#回溯法
"""
思路: xi的取值集合Ci={0,1},是否完整解 i=n 
剪枝:ck={0,1} 当重量小于背包容量时,才扩展解  ck={0}当重量大于yub背包容量时,不扩展解
"""


"""
global X=(x0,x1...)可行解,Ck(k=0,1,...)可扩展空间 Opt,OptX
procedure KNAPSACK(k,CurW):
    if k==n:  //检测是一个可行解
        Process2()   #获取可行解中值最大的
    if k==n:  #如果是最后一个，便结束
        Ck={}
    elif Curw+wk<=C:  //可扩展
        Ck={0,1}
    else:            //不可扩展
        Ck={0}
    for each x in Ck:
        X[k]=x  //扩展解
        KNAPSACK(k+1,CurW+xk*wk)  //递归调用
procedure Process2():
    global Opt,OptX
    Curv=p1*w1+p2*w2+...+pn*wn
    if Curv>Opt:
        Opt=Curv   #更新最优值
        OptX=X[:]  #更新最优解  
"""


#例二、团问题
'''
团:无向图,顶点子集S,任意两点都有一条边相连
空集,单个点，都是团
极大团:团S,不是其他团的真子集
最大团:顶点数最多的极大团
'''
#枚举所有的团
"""
1、
知道部分解[x0,x1,...,xk-1],且Sk-1={x0,x1,...,xk-1}是一个团
Ck={v∈V-Sk-1:(v,x)∈E for all x∈Sk-1}  #对于剩下的每个点,看是否每个点与Sk-1中的点都有边相连,如果是,则加入Ck可扩展解中。
存在问题:大小为K的团会被枚举K!次

2、每次减去更多的枝,来减少枚举次数
为顶点排序v0,v1,...,vn-1
Ck={v∈Ck-1:(v,xk-1)∈E and v>xk-1}  #如与加入第四个顶点全相连的点,肯定与前三个顶点全相连。故只需在上一次中的可行解中找。
Av={u∈V:(u,v)∈E}  #v的邻接点集合 即ck-1中每个点的邻接点集合
Bv={u∈V: u>v}  #v比V中的点大的点集合

"""

"""枚举所有团
procedure all_clique(k):
    if k==0:
        output([])
    else:
        output([x0,x1,...,xk-1])
    if k==0:
        Ck=V  #第一次时，可行解为全部V
    else:
        Ck=Axk-1 ∩ Bxk-1  ∩ Ck-1  #可行解为 上一次的可行解与 xk-1的邻接点集合与比xk-1大的点集合的交集
    for all x in Ck:
        X[k]=x
        all_clique(k+1)

"""

'''
枚举所有极大团
Nk =Ax-1 ∩Nk-1   为sk-1中每个顶点的邻接点的交集   如果sk-1中所有点的共同邻接点为空,那么他就是个极大团


globao X=(x0,x1,...,xk-1)  #可行解  Ck(k=0,1,...)可扩展空间 
if k==0:
    Nk=V   #第一次时，sk-1的邻接点集合交集为全部V
else:
    Nk=Axk-1 ∩ Nk-1  #所有可行解的共同邻接点集合
if Nk=={}: #如果为空,则为极大团
    output(X)
if k==0:
    Ck=V  #第一次时，可行解为全部V
else:
    Ck=Axk-1 ∩ Bxk-1  ∩ Ck-1  #可行解为 上一次的可行解与 xk-1的邻接点集合与比xk-1大的点集合的交集
for all x in Ck:
    X[k]=x
    all_max_clique(k+1)

'''



#三、集合覆盖问题
'''
集合R={0,1,...,n-1}  #n个元素
和R的子集族S,判断S是否包含一个R的覆盖
即 S'={S1,S2,...,Sm} 使得S1∪S2∪...∪Sm=R #S'中的每个集合都是S中的集合
且R中的元素在S'中只出现一次
'''

'''
方法一
构造无向图
当且仅当Si与Sj有交集为空时,在Si与Sj之间连一条边
若S'是R的一个覆盖,则S'对应必然是Ｇ中的一个极大团。
找出所有的极大团，然后判断是否满足条件
'''

'''
方法二：集合的字典序
T∈S,T的特征向量 如n=7时  T={0,3,6} 的特征向量是  [1001010]
T的排名: rank(T)=2^0+2^3+2^6=73
Su>Sv 当且仅当rank(Su)>rank(Sv)


将子集族S进行划分：H0，H1，H2，...，Hm
Hi是S中包含i，但不包含比i小的元素的子集。
故现在每次选时
C'=Axi-1 ∩ Bxi-1  ∩ C'xi-1  #可行解为 上一次的可行解与 xi-1的邻接点集合与比xi-1大的点集合的交集
Ck=Hk∩C'k

'''

#界限函数
'''
求最大值时
快速得到P(X)的近似值,一个上界 B(X)
剪枝: P(X)<=B(X)<=optP(X)  当P(x)的上界小于最优解时,剪枝

golbal X optP optX ck

X:可行解
optP:最优值
optX:最优解
ck:可扩展空间


procedure backtrack(k):
if [x0,x1,...,xk-1] is a solution:
    P=profit(x0,x1,...,xk-1)
    if P>optP:
        optP=P
        optX=[x0,x1,...,xk-1]
compute Ck
B=B(x0,x1,...,xk-1)
for all x ∈Ck:
    if B<=optP:#剪枝  (在本轮不会剪掉，在X=(x0,x1,...,xk-1,xk)时会剪掉。)
        return
    X[k]=x
    Backtrack(k+1)
backtrack(0)
'''



#四、背包问题
'''
01背包问题:(x0,x1,...,xk-1)∈{0,1}^n
分数背包:xi∈[0,1]
01背包问题是一个NP问题
分数背包存在O(nlogn)的贪心算法
'''
"""
贪心,将物品按照单位重量价值大小依次排序,然后放入物品
如果放入后超过了背包容量,则放入一部分
"""
