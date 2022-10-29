
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

"""
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