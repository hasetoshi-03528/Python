def head(ls):
    return [ls[0]]

def tail(ls):
    return ls[1:]

def rev(ls):
    if not ls:
        return ls
    else:
        return rev(tail(ls)) + head(ls)

L=[1,2,3]
c=2

print(rev(L))
