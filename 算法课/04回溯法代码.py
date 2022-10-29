
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








# 回溯法
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

