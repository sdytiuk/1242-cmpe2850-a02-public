from time import sleep
import time
import threading
import random

barrier = threading.Barrier(3)
myLock = threading.Lock()

print('Starting ...')
sleep( 1.55 ) #sleep for 1550ms
print('Done')
now = time.time()

while (time.time() - now < 2.5):
    time.sleep(0.1)
    print('.', end='')

print(f"Elapsed time : { time.time() - now} sec")

def SampleThread(exitNum, pChar='Z'):
    global myLock
    #exitNum = random.randint(10,20)
    print(f"EXIT NUM from Thread: [{exitNum}]")
    while True:
        time.sleep(0.3) #put sleep first so we don't forget it!!
        with myLock:
            currNum = random.randint(10,20)
        print(f"{pChar}.{currNum}.{pChar}", end="")
        if (exitNum == currNum):
            break
    print(f'{pChar}!{pChar}')
    barrier.wait() #put it at the end of the thread...

thr = threading.Thread(target=SampleThread, daemon=True, args=[16,])
thr.start()
print('Thread Started')
time.sleep(1)
thr2 = threading.Thread(target=SampleThread, daemon=True,
                        kwargs={'exitNum' : 19, 'pChar' : 'Y'})
thr2.start()
print('Thread2 Started')
time.sleep(1)
print("Main working")
#thr.join() #this makes the main thread "join" the thr thread and
#thr2.join()
barrier.wait()
#wait for it to finish
print('Main Done')
