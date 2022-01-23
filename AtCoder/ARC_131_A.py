import time
A   = int(input())
B   = int(input())
starttime   = time.time()
# 以下は全探索の例．TLE
#for x in range(A,int(1e18),1):
#    if str(A) in str(x):
#        if str(B) in str(2*x):
#            break
#        else:
#            pass
#    else:
#        pass
#print(x)

if A == B:
    pass
elif A > B:
    pass
elif A < B:
    pass
print(x)

endtime = time.time()
print("経過時間は{}秒".format(endtime-starttime))