def _sum(a):
    if len(a)==1:
        return a[0]
    else:
        return a.pop()+_sum(a)
print(_sum(list(map(int, input().split()))))