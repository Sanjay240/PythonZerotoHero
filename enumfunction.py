# use to simplgy the code
# 

l1 = ["aloo","Bhindi","chopsticks","chowmein"]

i = 1
for item in l1:
    if i%2 is not 0:
        print(f"item is {item}")
        i += 1
        
        
for index, item in enumerate(l1):
    if index%2 == 0:
        print(f"please buy {item}")