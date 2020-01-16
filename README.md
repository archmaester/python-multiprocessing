# python-multiprocessing

Data Science community struggles with handling large amount of data. 
Python provides various functionalities like mutliprocessing, multithreading modules, etc. 
In addition to this there are third party frameworks like Ray which provide and easy to use interface. 

The aim of this repository is to explore all these modules and provide a comparison like which module is best suited for which scenario. 

The file function_mp_python.py implements a test function which is executed using multiprocessing framework of python.

Consider a case where we have to do some computation on two variables a and b which take more than 1second to execute. The results of this is to be added to a variable sum variable. This is to be done for each iteration of the for loop. Each iteration in a for loop is independent of each other. 

If number of iterations is 1000, then serial execution will take atleast 1000s to execute. Our resources are not completely utilized. If the same thing is executed in parallel it would take around 2s considering some overhead which saves time.

The purpose of this function is to do that using multiprocessing module of python. My system has a 12 core CPU. Each function call takes approx 1s to execute
 ___________________________________________________
|Iterations | Parallel (seconds) | Serial (seconds) | 
|___________________________________________________|
|1000       | 4.2s               | 1000s            |
|10000      | 37.4s              | 10000s           | 
|___________________________________________________|

The variables in the python file should be adjust based on the computation power of the machine.














