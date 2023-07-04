#include<bits/stdc++.h>
using namespace std;

int main()
{
    int k,s;
    cin>>k>>s;
    int res=0;
    for(int i=0; i<=k; i++)
        for(int j=0; j<=k; j++)
        {
            int z=s-i-j;
            if(z>=0 && z<=k)
              res++;
        }
    cout<<res;
    return 0;
}
/*
K, S = map(int, input().split())

count = 0
for X in range(K+1):
    for Y in range(K+1):
        Z = S - X - Y
        if 0 <= Z <= K:
            count += 1

print(count)
*/
