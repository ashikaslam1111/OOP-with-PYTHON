
# def some(person):
#     print("hello",person)

# def some():
#     print("hello unknown")

# some('aslam')


def func(datatype,*args):
    if datatype =='int':
        print("integer")
        print('sting')
        ans = 0
        for i in args:ans+=i
        print(ans)
    if datatype=='str':
        print([args])
        


func('int',22,33)
func('int',"aslam","ashik")