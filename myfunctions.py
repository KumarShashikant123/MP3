def dinl(l1=[]):
    l=[]
    l=l1
    
    l2=[]

    for i in range(0,len(l)):
        n=list(l[i].values())
        l2.append(n)
    
    print(l2)






#more than one dictionaries in a list,fetching the value from each dict of a specific key, and placing it in a list
def dinl_samekey(l=[]):
    
    li1=[]
    li1=l
    li=[]
    i=0
    for i in range(i,len(li1)):
    
        n=(li1[i].get('s'))
        li.append(n)
    
    
    print(li)


#li2=[{'a':1,'s':2,'d':3,'f':4,'w':5},{'a':12,'s':33,'dd':56},{'a':1,'s':2,'d':3,'f':4,'w':5}]
#dinl_samekey(li2)





#A list having elements in which each element can contain comma or not,i have to seperate "," from the list which contains comma
#Finally make a list having no comma

def endcomma_fromlist(l=[]):
    l1=l
    newlist=[]
    for i in l:
        newlist.append(i.split(","))

    l2=[]

    for i in newlist:
        if len(i)<2:
            l2.append(i[0])
        else:
            j=0
            for j in range(j,len(i)):
                l2.append(i[j])
    return l2
    
    
            
    
#l1=['rahul','shashi,ravi','satish,chandra']
#endcomma_fromlist(l1)


   
