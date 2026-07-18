def prnt(n):
    print(n)
    if(n==0):
        return
    prnt(n-1)

prnt(8)
