f = lambda n:1 if n==0 or n==1 else n*f(n-1)
f(5)
print(f(5))