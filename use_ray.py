import ray
import time 

num_cpus = 12
num_workers = 12
max_iters = 15000
ray.init(num_cpus = num_cpus)

# make sure individual function takes some time if the time is too less then overhead of ray may decrease the performance compared to serial execution
@ray.remote(num_cpus = 1)
def test_function(a, b):
    time.sleep(1)
    return a + b

workers = [test_function for _ in range(num_workers)]

object_ids = []

start = time.time()

for ii in range(144):

    a = 1
    b = 1
    object_id = workers[int(ii%num_workers)].remote(a, b)
    object_ids.append(object_id)
    
    # use this 
    if ii % max_iters == 0 :
        ray.get(object_ids)
        object_ids = []

ray.get(object_ids)
print(time.time() - start)   

