x=int(input())
a=int(x/(60*60))
a1=x%(60*60)
b=int(a1/60)
c=a1%60
print(a,":",b,":",c, sep="")
