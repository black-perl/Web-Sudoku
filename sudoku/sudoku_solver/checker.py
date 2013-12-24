def empty_check(l,a):
    test=['1','2','3','4','5','6','7','8','9']
    l,n=l,a
    k=[]#list to store indices of the unfilled places
    for i in range(3*n):
        for j in range(3*n):
            if l[i][j] not in test:
                k.append([i,j])
            else:
                pass
    return l,k


def pack(l):
    length=9
    a,b=0,0
    pack=[]
    k=[]
    while a<length:
                 for i in range(a,a+3):
             
                    for j in range(b,b+3):
                                  k.append(l[i][j])
        
                 pack.append(k)
                 k=[]
                 if 0<= b< 6:
                         b=b+3
                         
                 else:      #use elif to create mutually exclusiveness
                           a=a+3
                           b=0
                           
                 
                    

    return pack


  
    
            
            
            
    
