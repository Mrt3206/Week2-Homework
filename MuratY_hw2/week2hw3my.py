flag=True
while flag:
    intext=input("Pls Enter Text :").lower().replace(" ","") #Text Enter
    inset=set(intext)
    froinse=frozenset(inset)
    inlist=list(intext)
    outletter={}
    for i in froinse:
        a=inset.pop()
        outletter[a]=inlist.count(a)   
    print(list(sorted(outletter.items())))
    secim=input("\n\n(N)ew Text,  (E)xit : ").upper()
    while True:
        if secim=="N":
            flag=True
            break
        elif secim=="E":
            flag=False
            print("See you Later...")
            break
        
        else:
            print("New Text N , Exit E Enter: ")
            secim=input("(N)ew,  (E)xit : ").upper()  
