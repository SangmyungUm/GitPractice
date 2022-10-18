h,m=map(int,input().split())


if m-45<0:
    H=h-1
    if H<=-1:
        H=23
    M=60+(m-45)
else:
    H=h
    M=m-45
print(H,M)
