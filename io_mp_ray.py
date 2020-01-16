import ray
import time 
import os 
import cv2

total_iters = 10000
image_path = './input.jpg'
output_path = "./outputs"

if not os.path.exists(output_path):
    os.makedirs(output_path)
    
#########################################################
        # Parallel Execution of test function #
#########################################################

# Get the number of cpus or manually define how many cpus you want to use
num_cpus = os.cpu_count()
print (" Using {} CPUs for processing.".format(num_cpus)) 

# Manually define the number of workers the default is set to number of CPUs
num_workers = num_workers = max(num_cpus, 30)
print ("Initializing {} workers for processing.".format(num_workers)) 

# Initialize ray
ray.init(num_cpus = num_cpus)

# Define a test function which should be executed parallely, default num of cpus is 1, change it as required
@ray.remote
def test_function_parallel(ii, image_path):
    
    img = cv2.imread(image_path)
    cv2.imwrite(os.path.join(output_path, str(ii) + ".jpg"), img)

    return 

# Initialize the workers
workers = [test_function_parallel for _ in range(num_workers)]

a = 1
b = 1
max_iters = min(10000, total_iters - 1)
object_ids = []
start = time.time()
for ii in range(total_iters):

    object_id = workers[int(ii%num_workers)].remote(ii, image_path)
    object_ids.append(object_id)
    
    # after max_iters the objects are fetched before processing further iterations
    if ii % max_iters == 0 or ii == len(range(total_iters)):
        ray.get(object_ids)
        object_ids = []

# get remaining objects
ray.get(object_ids)
print("Time taken by Parallel Execution in seconds : ", time.time() - start)   


# #########################################################
#         # Serial Execution of test function #
# #########################################################

# def test_function_serial(ii, a, b):

#     img = cv2.imread(image_path)
#     cv2.imwrite(os.path.join(output_path, str(ii) + ".jpg"), img)
    
#     return

# a = 1
# b = 1
# start = time.time()
# for ii in range(total_iters):
#     test_function_serial(ii,a,b)
    
# print("Time taken by Serial Execution in seconds : ", time.time() - start)   
