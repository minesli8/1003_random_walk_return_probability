'''
The partical starts at (0, 0, ..., 0) (Origin in the n-dimensional Euclidean space).
after 1 step, the position of the particle is (d_11, d_12, ..., d_1n);
after 2 steps, the position is (d_11+d_21, d_12+d_22, ..., d_1n+d_2n);
...
after M steps, the position is (d_11+d_21+...+d_M1, ..., d_1n+d_2n+...+d_Mn).
Here d_ij = 1 or -1.
'''
import numpy as np
import random
import multiprocessing as mp
import time


# M_total is the maximum number of steps for each simulation.
M_total = int(1e4)

def returned(n):

    M = M_total

    flag = 0
    pos = [[0]*n] #Initial position of the particle is the origin.
    for i in range(1, M):
        temp = [0]*n

        direction = random.sample([x for x in range(n)], 1)
        
        for j in range(n):
            r = np.random.uniform(0,1)
            if(r<0.5):
                d = -1
            else:
                d = 1
            if(j==direction[0]):
                temp[j] = pos[i-1][j] + d
            else:
                temp[j] = pos[i-1][j]
                          
        
        pos.append(temp)
        if(pos[i]==[0]*n):
            flag = 1
            break
            
    return(flag)



####################################################
####################################################
####################################################
if __name__ == '__main__':
    n_simulation = int(1e3)

    start_time = time.time()

    report = open('./result_2d.txt', 'w')
    report.write('For M=%d, n_simulation=%d : \n' %(M_total, n_simulation))



    # 2-dim:   
    n = 3

    inputs = [n]*n_simulation
    pool = mp.Pool(processes=4)
    flags = pool.map(returned, inputs)
    
    count = sum(flags)            
    print('For 2-dimension, the probability is:')
    p = count/n_simulation
    print(p)
    report.write('For 2-dimension, the probability is:\n')
    report.write('%f\n' %(p))
    
    

    end_time = time.time()
    elapsed_time = end_time - start_time
    print('Total elapsed time: %f' %(elapsed_time))
    report.write('Total elapsed time for parallel code: %f' %(elapsed_time))

    report.close()



