import sys
x=int(sys.argv[1])
y=x-1
i=1
j=1
def uptriangle(x):
    global i
    print(" "*(x-1)+"*"*((i*2)-1)+" "*(x-1))
    i=i+1
    x=x-1
    if x!=0:
        return uptriangle(x)
def downtriangle(y):
    global j
    print(" "*(j)+"*"*((y*2)-1)+" "*(j))
    j=j+1
    y=y-1
    if y!=0 and y>0:
        return downtriangle(y)
uptriangle(x)
downtriangle(y)