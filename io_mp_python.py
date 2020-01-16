import ray
import time 
import os 
import cv2
from multiprocessing import Process, cpu_count, Manager

total_iters = 10000
image_path = './input.jpg'
output_path = "./outputs"

if not os.path.exists(output_path):
    os.makedirs(output_path)
    
#########################################################
        # Parallel Execution of test function #
#########################################################

start_time = time.time()

# max 1000 processes can be called 
max_iters = min(2000, total_iters)
processes = []

def test_function_parallel(ii, image_path):

    img = cv2.imread(image_path)
    cv2.imwrite(os.path.join(output_path, str(ii) + ".jpg"), img)
    
    return

start = time.time()
for ii in range(total_iters):
    
    pcs = Process(target = test_function_parallel, args=(ii, image_path))
    processes.append(pcs)
    pcs.start()
    
    if ii % max_iters == 0 or ii == len(range(total_iters)) - 1:  
        
        for jj in range(len(processes)): 
            processes[jj].join()
        processes = []

for jj in range(len(processes)): 
    processes[jj].join()        

print("Time taken by Parallel Execution in seconds : ", time.time() - start)  

# #########################################################
#         # Serial Execution of test function #
# #########################################################

# def test_function_serial(ii, image_path):

#     img = cv2.imread(image_path)
#     cv2.imwrite(os.path.join(output_path, str(ii) + ".jpg"), img)
    
#     return


# a = 1
# b = 1
# start = time.time()
# for ii in range(total_iters):
#     test_function_serial(ii, image_path)
    
# print("Time taken by Serial Execution in seconds : ", time.time() - start)   
