firstset=set(input("Pls Enter First Word: ")) #first word
secondset=set(input("Pls Enter Second Word: "))#second word
intlist=sorted(firstset&secondset) #intersection list
uniqw1=sorted(firstset-secondset) #w1-w2 list
uniqw2=sorted(secondset-firstset) #w2-w1 list
print([''.join(intlist),''.join(uniqw1),"".join(uniqw2)]) #output