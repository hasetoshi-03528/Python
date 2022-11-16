def num_con(d, r):
    X_dumy = d
    out = ''
    while X_dumy>0:
        out = str(X_dumy%r)+out
        X_dumy = int(X_dumy/r)
    return out

d=int(input("d="))
r=int(input("r(2-9)="))
print(num_con(d,r))
