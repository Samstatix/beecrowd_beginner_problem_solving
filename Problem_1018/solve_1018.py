x=int(input())
print(x)
a=int(x/100)
print(a, "nota(s) de R$ 100,00")
a1=x%100
b=int(a1/50)
print(b, "nota(s) de R$ 50,00")
b1=a1%50
c=int(b1/20)
print(c, "nota(s) de R$ 20,00")
c1=b1%20
d=int(c1/10)
print(d, "nota(s) de R$ 10,00")
d1=c1%10
e=int(d1/5)
print(e, "nota(s) de R$ 5,00")
e1=d1%5
f=int(e1/2)
print(f, "nota(s) de R$ 2,00")
f1=e1%2
g=int(f1/1)
print(g, "nota(s) de R$ 1,00")
