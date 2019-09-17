def fibo(n):
    if n in memo:
        return memo[n]
    if n==1:
        memo[1]=0
        return memo[1]
    if n==2:
        memo[2]=1
        return memo[2]
    else:
        memo[n]=fibo(n-1)+fibo(n-2)
        return memo[n]
def fib(n):
    if n==1:
        return 0
    if n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
memo={}  
n=int(input())
a=fibo(n)
for i in range(1,n):
    print(memo[i], end=' ')

