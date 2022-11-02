
def add_chain(chains):
    global opt_chains
    if chains[-1]==target:       #如果最后一个是目标值，就返回
        if len(chains)<len(opt_chains):
            opt_chains=chains[:]
        return
    elif chains[-1]>target:      #如果最后一个大于目标值，就返回
        return
    else:
        Ck=[] #计算可扩展空间
        for i in chains[::-1]:
            j=chains[-1]+i
            if (j)<=target and (j)>chains[-1] and (len(chains)+1)<len(opt_chains) and (j) not in Ck :
                if len(chains)!=target+1: #找到了一个解
                    sum=j
                    for _ in range(len(opt_chains)-len(chains)-1):
                        sum*=2
                    if sum<target:
                        continue
                Ck.append(j)
        for i in Ck:
            chains.append(i)
            add_chain(chains)
            chains.pop()        #回溯,去掉刚才添加的最后一个元素




def find_shortest_chains(target):
    chains=[1,2]
    target=target   #目标值
    global opt_chains
    opt_chains=[0 for i in range(target+1)]   #最优解
    add_chain(chains)  #找到所有解，记录在answer_chains中
    
    print(opt_chains)
if __name__=='__main__':
    target=607
    find_shortest_chains(target)