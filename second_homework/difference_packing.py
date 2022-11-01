def traceback(v,k,n,X):
    if k==n:        
        global answer
        print(X)    
        answer.append(X[:])
        # difference=[]
        # for i in X:
        #     for j in X:
        #         difference.append((i-j+v)%v)
        # print(difference,len(difference))
    else:
        difference=[]
        for i in X:
            for j in X:
                difference.append((i-j+v)%v)
        difference=set(difference)
        ck=[]
        for i in range(0,v):
            if i not in X :
                for j in X:
                    if (i-j+v)%v  in difference or (j-i+v)%v  in difference or (i-j+v)%v==(j-i+v)%v:  #剪枝
                        break
                else:
                    ck.append(i)
        for x in ck:
            X.append(x)
            traceback(v, k+1, n, X)
            X.pop(-1)
def difference_packing(v,n):
    global answer
    answer=[]
    traceback(v,0,n,[])
    # print("(%d,%d) answer: %s"%(v,n,str(answer)))

# difference_packing(13, 4)
difference_packing(31, 6)