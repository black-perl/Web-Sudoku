def colrow(k,l,a,b):
    lis1=[l[s][b] for s in range(0,9)]
    lis2=l[a]
    lis3=[]
    test=['1','2','3','4','5','6','7','8','9']
    if lis1.count('')==2 and k not in lis1 and k not in lis2:
        lis3=lis3 + lis1
        lis3.append(k)
        for x in test:
            if x not in lis3:
                dummy=x
                if dummy in lis2:
                  return True
                else:return False
            
    elif lis2.count('')==2 and k not in lis2 and k not in lis1:
         lis3=lis3 + lis2
         lis3.append(k)
         for x in test:
            if x not in lis3:
                dummy=x
                if dummy in lis1:
                    return True
                else: return False
            
    else:
        return False 
        
         
