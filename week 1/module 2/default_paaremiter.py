# s = input()
# n = len(s)

# i=0
# while(i<n):
#     if(s[i]=='.'):
#         print('0',end="")
#     elif(s[i]=='-' and s[i+1]=='.'):
#         print('1',end="") 
#         i+=1
#     elif(s[i]=='-' and s[i+1]=='-'):
#         print('2',end="") 
#         i=i+1  
#     i+=1        

def hello(a,b,c=0):
    return a+b+c

print(hello(1,3,9 ))