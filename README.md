# MultiThreading-Python

### Simple Program

#### Output -> Using only the Main thread 


![alt text](https://github.com/gokulraviteja/Threading-Python/blob/master/screenshots/output1.png)


If we need to make one lakh calls ,which is a general requirement at company level , 
Time = (44.86/50)*100000 = approx 89720 sec = approx 1 day 

![alt text](https://github.com/gokulraviteja/Threading-Python/blob/master/screenshots/code1.png)


#### Output -> Creating a new thread for each call

![alt text](https://github.com/gokulraviteja/Threading-Python/blob/master/screenshots/output21.png)

Time = (2.7/50)*100000 = 5400 sec = approx 1.5 hours

![alt text](https://github.com/gokulraviteja/Threading-Python/blob/master/screenshots/code2.png)


But creating a new thread for each and every call is not a good practice , by the eod we have some constraints on speed, space everywhere ..


Here we need to consider the constraint on the number of threads and there by distributing the calls to those threads.

![alt text](https://github.com/gokulraviteja/Threading-Python/blob/master/screenshots/code3.png)


## Happy Threading!!


