#indirectly bounded columns
def col_check(k,l,a,b):
   for n in range(3):
        for m in range(3):
            if (3*m) <= a < ((3*m)+3) and (3*n) <= b < ((3*n)+3):

                if b==(3*n):
                    rule1=k in [l[s][b+1] for s in range(0,9)]
                    rule2=k in [l[s][b+2] for s in range(0,9)]
                    return (rule1 and rule2)
                elif b==((3*n)+2):
                    rule1=k in [l[s][b-1] for s in range(0,9)]
                    rule2=k in [l[s][b-2] for s in range(0,9)]
                    return (rule1 and rule2)
                    
                else: 
                    rule1=k in [l[s][b+1] for s in range(0,9)]
                    rule2=k in [l[s][b-1] for s in range(0,9)]
                    return (rule1 and rule2)
      

     
