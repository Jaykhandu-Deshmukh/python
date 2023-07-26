import time
initial=time.time()
k=0
while(k<45):
    print("hello")
    k+=1
print(("while", time.time()-initial))

initial2=time.time()
for i in range(45):
    print("hello")
print(("while", time.time()-initial))

localtime=time.asctime(time.localtime(time.time()))
print(localtime)