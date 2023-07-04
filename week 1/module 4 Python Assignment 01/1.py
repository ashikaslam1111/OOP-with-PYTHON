s= input()
n=len(s)
st =0
tota =0
the_list=[]
for i in range(0,n):
    l = s[st:i+1]
    r= s[i+1:n-1]
    ll =  l.count('L')
    lr=l.count('R')
    rl =r.count('L')
    rr =r.count('R')
    if ll==lr:
        tota+=1
        the_list.append(l)
        st=i+1
print(tota)
for i in the_list:
    print(i)
    
    