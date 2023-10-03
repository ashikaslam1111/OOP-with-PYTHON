import math
import time
def timer(func):
   def inner(*args,**arg):
       st = time.time()
       func(*args,**arg)
       fin =time.time()
       print(fin-st)
   return inner

    
    






@timer
def get_facto(n):
    print(f"factorial is {math.factorial(n)}")

print(get_facto(n=5))

