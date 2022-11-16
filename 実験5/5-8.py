def fib_r(seq):
    if seq<=1:
        return seq
    return (fib_r(seq-1) + fib_r(seq-2))

n=int(input("n="))
print(fib_r(n-1))
