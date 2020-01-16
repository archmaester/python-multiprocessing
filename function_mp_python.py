from multiprocessing import Process, cpu_count, Manager
import ray
import time 
import os 

total_iters = 1000
sleep_time = 1

#####################################################################################################
            # Parallel Execution of test function using Python Multiprocessing#
#####################################################################################################

sums = 0 
manager = Manager()
return_dict = manager.dict() # dict, list , array etc. 

def test_function_parallel(return_dict, ii, a, b):
    time.sleep(sleep_time)
    # Use below line in case you want to return something from function 
    return_dict[ii] = a + b
    return

start_time = time.time()

# max 1000 processes can be called 
max_iters = min(1000, total_iters)

processes = []
sums = 0

for ii in range(total_iters):
      
    a = 1
    b = 1
    pcs = Process(target = test_function_parallel, args=(return_dict, ii, a, b))
    processes.append(pcs)
    pcs.start()
    
    if ii % max_iters == 0 or ii == len(range(total_iters)) - 1:  
        
        for jj in range(len(processes)): 
            processes[jj].join()
        processes = []
        
for key in return_dict:
    sums += return_dict[key]

return_dict = {}  
              
sums += sum(return_dict)    
print("Time taken by Parallel Execution in seconds : ", time.time() - start_time, sums)  

# #########################################################
#         # Serial Execution of test function #
# #########################################################

# def test_function_serial(ii, a, b):
#     time.sleep(sleep_time)
#     print(ii)
#     return a + b

# a = 1
# b = 1
# start = time.time()
# for ii in range(total_iters):
#     test_function_serial(ii, a,b)
    
# print("Time taken by Serial Execution in seconds : ", time.time() - start)   