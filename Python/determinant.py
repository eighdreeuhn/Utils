f=lambda x:1if x<2else x*f(x-1)%x
ritual=lambda n:1 if n < 2 else f(f(n))
print(ritual(10))
