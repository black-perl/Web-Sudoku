#indirectly bounded rows
def row_check(k,l,a,b):
    for m in range(3):
        for n in range(3):
            if (3*m) <= a < ((3*m)+3) and (3*n) <= b < ((3*n)+3):

                if a==(3*m):
                    rule1=k in l[a+1]
                    rule2=k in l[a+2]
                    return rule1 and rule2
                elif a==((3*m)+2):
                    rule1=k in l[a-1]
                    rule2=k in l[a-2]
                    return rule1 and rule2
                else:
                    rule1=k in l[a+1]
                    rule2=k in l[a-1]
                    return rule1 and rule2
      

                    
                    
                
