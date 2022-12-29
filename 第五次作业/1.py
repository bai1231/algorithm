


G={'S':{'A':(0,7),'B':(0,6)},'A':{'C':(0,4),'D':(0,2)},'B':{'C':(0,2),'D':(0,3)},'C':{'T':(0,9)},'D':{'T':(0,5)}}  #(flow,capacity)
#利⽤Ford-Fulkerson 求最小割，最⼤流
def Ford_Fulkerson(G,s,t):
    #初始化Residual network
    R={}
    for u in G:
        R[u]=dict.get(R,u,{})
        for v in G[u]:
            R[u][v]=G[u][v][1]
            R[v]=dict.get(R,v,{})
            R[v][u]=0
    #初始化flow
    flow=0
    while True:
        #找到一条从s到t的增广路径
        path=FindPath(R,s,t)
        if path==None:
            break
        #找到路径上的最小容量
        min_capacity=FindMinCapacity(R,path)
        #更新flow
        flow+=min_capacity
        #更新Residual network
        for i in range(len(path)-1):
            R[path[i]][path[i+1]]-=min_capacity
            R[path[i+1]][path[i]]+=min_capacity
    return flow,R
#利用深度优先搜索找到一条从s到t的路径
def FindPath(R,s,t):
    path=[s]
    visited=[s]
    while len(path)>0:
        u=path[-1]
        for v in R[u]:
            if v not in visited and R[u][v]>0:
                path.append(v)
                visited.append(v)
                break
        else:
            path.pop()
        if  len(path)>0 and path[-1]==t :
            return path
    return None

#找到增广路径上的最小容量
def FindMinCapacity(R,path):
    min_capacity=R[path[0]][path[1]]
    for i in range(len(path)-1):
        if R[path[i]][path[i+1]]<min_capacity:
            min_capacity=R[path[i]][path[i+1]]
    return min_capacity


#找到最大流
def FindMaxFlow(G,s,t):
    flow,R=Ford_Fulkerson(G,s,t)
    return flow,R

#主函数
if __name__=='__main__':
    s='S'
    t='T'
    flow,R=FindMaxFlow(G,s,t)
    print('最大流为：',flow)
    print('最小割=最大流：',flow)


