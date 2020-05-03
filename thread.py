import requests
import json
import time
import util as ut # custom template

def apiCall(i):
	try:
		url = 'http://dummy.restapiexample.com/api/v1/create'

		data={"name":"test","salary":"123","age":"23"}

		r = requests.post(url,data=json.dumps(data))

		d=(r.content).decode("utf-8") 

		ut.fw("thread/"+str(i)+".txt",d,'w')  # write content to a file

		return True

	except:

		return False

parameters=range(1,51)
for i in parameters:
	apiCall(i)


n=time.time()
print("Plain , With only Main Thread")
print(time.time()-n, "seconds for 50 Calls")



from threading import Thread

threads=[]
for i in parameters:
    process = Thread(target=apiCall, args=[i])
    process.start()
    threads.append(process)

for process in threads:
    process.join()

n=time.time()
print("Creating one thread for every call ")
print(time.time()-n, "seconds for 50 Calls")





from Queue import Queue
from threading import Thread

q = Queue(maxsize=0)

num_threads = min(50, len(parameters))



for i in parameters:
    q.put(i)

def helper(q):
    while not q.empty():
        work = q.get()                      
        apiCall(work)
        q.task_done()
    return True

for i in range(num_threads):
    worker = Thread(target=helper, args=[q])
    worker.setDaemon(True)
    worker.start()
q.join()

n=time.time()
print("By maintaining limited threads and using Queue for allocating")
print(time.time()-n, "Seconds for 50 Calls")
