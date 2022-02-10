strlist=str(input("Pls Enter List like  [1,2,3,4,5] :  "))
n=int(input("Pls Enter Shift Number: "))
orilist=[] # Original List
for i in strlist:
    if i != '['and i!=']' and i!=',':
        orilist.append(int(i))
print(len(orilist))
cpylist=[x for x in range(len(orilist))] # Copy List
for j in range(len(orilist)):
    if (j+n)<len(orilist):    
        cpylist[n+j]=orilist[j]
    else:
       cpylist[(j+n)-len(orilist)]=orilist[j]
        
print(cpylist)