
def timer(func):
    func()
    def inner():
        print("time started")

        print("time ended")
    return inner

#timer()()
@timer # digital way to make decotaor
def get_factorial():
    print("factorial starting")

get_factorial() # nown it means the 16 line with out  @timer 
## timer(get_factorial)() analog way to make decorator