f=open('x.csv','r')
txt=f.read()
f.close()
list1=txt.split('\n')
X=[]
#print(list1[1::])
for i in list1[1::]:
    elem=i.split(',')
    r=[float(item) for item in elem if len(item)>0]
    X.append(r[1::])
print(X)

