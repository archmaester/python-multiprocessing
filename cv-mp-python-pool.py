from multiprocessing import Process, Manager, Pool
import time 
from tqdm import tqdm
import cv2
import os 
output_path = "./outputs"
resize = 120 
count = 0

def test_function_parallel(image_path):
    global count
    # Start delimiter   
    got_data = resize
    
    # Your code goes here 
    img = cv2.imread(image_path) # Sample
    img = cv2.resize(img, (got_data, got_data))
    cv2.imwrite(os.path.join(output_path, str(count) + ".jpg"), img) # Sample
    count += 1
    return 

def test_function_serial(identity, image_path, output_path, receive_data):
    
    # Your code goes here 
    img = cv2.imread(image_path) # Sample
    img = cv2.resize(img, (receive_data, receive_data))
    cv2.imwrite(os.path.join(output_path, str(identity) + ".jpg"), img) # Sample
    
    return 


def main():
    
    pool = Pool(processes= os.cpu_count()) 
    
    # Give path to your image
    image_path = './input.jpg'
    images_path = [image_path]*10000
    
    if not os.path.exists(output_path):
        os.makedirs(output_path)
        
    start_time = time.time()
    pool.map(test_function_parallel, images_path)
             
    print("Time taken by Parallel Execution in seconds : ", time.time() - start_time)
    
                                   
    # Serial Execution
    start_time = time.time() 
    for ii, image_path in enumerate(tqdm(images_path)):

        send_data1 = 120
        test_function_serial(ii, image_path, output_path, send_data1)
             
    print("Time taken by Serial Execution in seconds : ", time.time() - start_time)                     
    
if __name__== "__main__":
    main()