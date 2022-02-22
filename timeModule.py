import time

initial = time.time()
k = 0

while(k<45):
   # print("This is harry habit")
    k += 1
    
print(f"while loop runs in {time.time()-initial}")

initial2 = time.time()

for i in range(45):
   # print("this is a new habit")
   j = i

print(f"for loop runs in {time.time()- initial2}")

localtime = time.asctime(time.localtime(time.time()))
print(localtime)

# use time.sleep to sleep let the program to wait.