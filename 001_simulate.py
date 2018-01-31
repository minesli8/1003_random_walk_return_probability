N = 1000

N_rt = 0

max_steps = 10000

from scipy import random

for i in range(0, N):
    step = 0
    x=0
    while(step<max_steps):
        p = random.uniform(0,1)
        if(p>0.5):
            x += 1
        else:
            x -= 1

        step += 1

        if(x==0):
            N_rt += 1
            break


prob = float(N_rt/N)

file = open('./result.txt','w')
file.write("The probability of returning is "+str(prob))
file.close()
