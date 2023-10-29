/* Program to raise x^n using O(logN) Complexity */
#include<iostream>
using namespace std;

int main()
{
    long long res = 1;

    long long x, n, n1, x1;

    cin>>x>>n;
    n1 = n;
    x1 = x;

    while (n > 0)
    {
        if (n % 2 == 1)
            res = res * x;
        
        x = x * x;
        n >>= 1;
    }

    cout<<x1<<"^"<<n1<<"="<<res;
    return 0;
}