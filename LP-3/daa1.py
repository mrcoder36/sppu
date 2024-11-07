# # recursive program


n= int(input("Enter the term :- "))
def rf(n):
    if n<=1:
        return n
    else:
        return rf(n-1)+rf(n-2)
    
if n <= 1:
    print(n)
else:
    for i in range(0,n+1):
        print(rf(i))
print(" Fibonacci numbers")    
print(f"The term number {n} and value is {rf(n)}")


# # non-recursive
# n= int(input("Enter the term :- "))
def iter(n):
    n1=0
    n2=1
    for i in range(1,n):
        n0=n1
        n1=n2
        n2=n0+n1
        print(n2)
        
    return n2
        
print(" Fibonacci numbers")
print(f"fibo {n} is {iter(n)}")

