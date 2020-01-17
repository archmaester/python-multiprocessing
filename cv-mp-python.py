from multiprocessing import Process, Manager
import time 
from tqdm import tqdm
import cv2
import os 

class FastDataProcessing(object):
    
    def __init__(self, max_processes = 1000):
        
        self.processes = []
        self.max_processes = max_processes
        
    def create_and_start_process(self, target_function, args):
        
        pcs = Process(target = target_function, args = args)
        self.processes.append(pcs)
        pcs.start() 
        
    def join_processes(self):
         
        for jj in range(len(self.processes)): 
            self.processes[jj].join()
        self.processes = [] 

def test_function_parallel(identity, image_path, output_path, receive_data):

    # Start delimiter   
    got_data = receive_data[identity]
    del receive_data[identity]
    
    # Your code goes here 
    img = cv2.imread(image_path) # Sample
    img = cv2.resize(img, (got_data, got_data))
    cv2.imwrite(os.path.join(output_path, str(identity) + ".jpg"), img) # Sample

    return 

def test_function_serial(identity, image_path, output_path, receive_data):
    
    # Your code goes here 
    img = cv2.imread(image_path) # Sample
    img = cv2.resize(img, (receive_data, receive_data))
    cv2.imwrite(os.path.join(output_path, str(identity) + ".jpg"), img) # Sample
    
    return 

def main():
    
    process_manager = FastDataProcessing()
    resource_manager = Manager()
    send_data = resource_manager.dict() 
    
    # Give path to your image
    image_path = './input.jpg'
    images_path = [image_path]*10000
    output_path = "./outputs"
    if not os.path.exists(output_path):
        os.makedirs(output_path)
        
    start_time = time.time()
    
    # Parallel Execution
    for ii, image_path in enumerate(tqdm(images_path)):
        
        send_data[ii] = 120
        process_manager.create_and_start_process(test_function_parallel,  \
                                                 args = (ii, image_path, output_path, send_data))
        
        if ii % process_manager.max_processes == 0 or ii == len(images_path) - 1:
                                    
            process_manager.join_processes()
             
    print("Time taken by Parallel Execution in seconds : ", time.time() - start_time)
    
                                   
    # Serial Execution
    start_time = time.time() 
    for ii, image_path in enumerate(tqdm(images_path)):

        send_data1 = 120
        test_function_serial(ii, image_path, output_path, send_data1)
             
    print("Time taken by Serial Execution in seconds : ", time.time() - start_time)                     
    
if __name__== "__main__":
    main()