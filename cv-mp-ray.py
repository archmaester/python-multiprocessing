import ray
import time 
from tqdm import tqdm
import cv2
import os 

#########################################################
        # Parallel Execution of test function #
#########################################################

# Get the number of cpus or manually define how many cpus you want to use
num_cpus = os.cpu_count()
print (" Using {} CPUs for processing.".format(num_cpus)) 

# Manually define the number of workers the default is set to number of CPUs
num_workers = num_workers = max(num_cpus, 100)
print ("Initializing {} workers for processing.".format(num_workers)) 

# Initialize ray
ray.init(num_cpus = num_cpus)
        
@ray.remote
def test_function_parallel(identity, image_path, output_path, receive_data):
    
    # Your code goes here 
    img = cv2.imread(image_path) # Sample
    img = cv2.resize(img, (receive_data, receive_data))
    cv2.imwrite(os.path.join(output_path, str(identity) + ".jpg"), img) # Sample

    return 

def test_function_serial(identity, image_path, output_path, receive_data):
    
    # Your code goes here 
    img = cv2.imread(image_path) # Sample
    img = cv2.resize(img, (receive_data, receive_data))
    cv2.imwrite(os.path.join(output_path, str(identity) + ".jpg"), img) # Sample
    
    return 

def main():

    # Initialize the workers
    workers = [test_function_parallel for _ in range(num_workers)]
    max_iters = 10000   
    # Give path to your image
    input_path = './input.jpg'
    images_path = [input_path]*10000
    output_path = "./outputs"
    if not os.path.exists(output_path):
        os.makedirs(output_path)
        
    start_time = time.time()
    object_ids = []
    
    # Parallel Execution
    for ii, image_path in enumerate(tqdm(images_path)):
        
        receive_data = 120
        object_id = workers[int(ii%num_workers)].remote(ii, image_path, output_path, receive_data)
        object_ids.append(object_id)

        # after max_iters the objects are fetched before processing further iterations
        if ii % max_iters == 0 or ii == len(images_path) - 1:
            ray.get(object_ids)
            object_ids = []
             
    print("Time taken by Parallel Execution in seconds : ", time.time() - start_time)
    
                                   
    # Serial Execution
    start_time = time.time() 
    for ii, image_path in enumerate(tqdm(images_path)):

        send_data1 = 120
        test_function_serial(ii, image_path, output_path, send_data1)
             
    print("Time taken by Serial Execution in seconds : ", time.time() - start_time)                     
    
if __name__== "__main__":
    main()