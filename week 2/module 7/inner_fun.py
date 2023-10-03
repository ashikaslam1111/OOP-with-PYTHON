# functon is fistclass object in python
# in python where a function can take anoter functon as argument
def outer():
    print("outt")
    def inner():
       return 'in'
    return inner
   
def do ():
    print('working')
    
def ala(fun):
    fun()
ala(do) # taking function as argument



# print(outer()())