import sys
x=int(sys.argv[1])
uptriangle={i:(i*2-1)for i in range(1,x+1)}
upspace={i:(x-i)for i in range(1,x+1)}
downtriangle={i:2*(x-1-i)+1 for i in range(1,x)}
downspace={i:i for i in range(1,x)}
upoutput=[" "*upspace.get(i)+"*"*uptriangle.get(i)+" "*upspace.get(i)+"\n" for i in uptriangle.keys()]
downoutput=[" "*downspace.get(i)+"*"*downtriangle.get(i)+" "*downspace.get(i)+"\n" for i in downtriangle.keys()]
stroutput=""
for x in upoutput:
    stroutput+=x
for x in downoutput:
    stroutput+=x
print(stroutput)