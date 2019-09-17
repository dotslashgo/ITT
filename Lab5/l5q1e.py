def _sum(n):
    if n==1:
        return 1
    return n+_sum(n-1)
print('Sum: ',_sum(int(input('Enter the value of n: '))))
