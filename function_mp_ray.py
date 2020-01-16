import ray
import time 
import os 

total_iters = 10000
sleep_time = 0.01

#########################################################
        # Parallel Execution of test function #
#########################################################

# Get the number of cpus or manually define how many cpus you want to use
num_cpus = os.cpu_count()
print (" Using {} CPUs for processing.".format(num_cpus)) 

# Manually define the number of workers the default is set to number of CPUs
num_workers = min(total_iters, 20)
print ("Initializing {} workers for processing.".format(num_workers)) 

# Initialize ray
ray.init(num_cpus = num_cpus)

# Define a test function which should be executed parallely, default num of cpus is 1, change it as required
@ray.remote
def test_function_parallel(ii, a, b):
    time.sleep(sleep_time)
    return a + b

# Initialize the workers
workers = [test_function_parallel for _ in range(num_workers)]

sums = 0 
max_iters = min(10000, total_iters - 1)
object_ids = []
start = time.time()
for ii in range(total_iters):
    
    a = 1 # args, change
    b = 1 # args, change
    object_id = workers[ii%num_workers].remote(ii, a, b) # call, change
    object_ids.append(object_id)

    # after max_iters the objects are fetched before processing further iterations
    if ii % max_iters == 0 or ii == len(range(total_iters)):
        sums += sum(ray.get(object_ids))
        object_ids = []
        
# get remaining objects
sums += sum(ray.get(object_ids)) # return values, change
print("Time taken by Parallel Execution in seconds : ", time.time() - start, sums)  

#########################################################
        # Serial Execution of test function #
#########################################################

# def test_function_serial(a, b):
#     time.sleep(sleep_time)
#     return a + b

# a = 1
# b = 1
# start = time.time()
# for ii in range(total_iters):
#     test_function_serial(a,b)
    
# print("Time taken by Serial Execution in seconds : ", time.time() - start)   
