import math 
def traceback(k,n,X,T):
    if k==n: #是一个解
        max_s=0
        for i in range(-2,n-2):
            if X[i]+X[i+1]+X[i+2]>max_s:
                max_s=X[i]+X[i+1]+X[i+2]
        global optS,optX
        if max_s<optS:
            optS=max_s
            optX=X[:]
            # print(optX,optS)
        return
    else:
        if k>=3:
        #剪枝
            # print(X)
    
            if X[-1]+X[-2]+X[-3]<avg_sum-2:
                return   
            if X[-1]+X[-2]+X[-3]>T: #三个数之和最大小于T
                return
            if X[-1]+X[-2]+X[-3]>optS:
                return
            
        ck=[i for i in range(1,n+1) if i not in X ]  #计算可扩展空间

        for x in ck:
            X.append(x)
            traceback(k+1,n,X,T)
            X.pop(-1)


def find_three_sum(n,T):
    global optS,optX,avg_sum
    optS=1000000 #无穷大
    optX=[]
    avg_sum=int(math.ceil((1+n)*3/2))
    traceback(0,n, [],T)
    return (optX,optS)

print(find_three_sum(12,21))
print(find_three_sum(13,23))
print(find_three_sum(14,24))
print(find_three_sum(15,25))
