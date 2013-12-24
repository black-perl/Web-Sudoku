#checks along a column in a row
def row_bound(k,l,a,b):
     for m in range(3):
        for n in range(3):
            if (3*m) <= a < ((3*m)+3) and (3*n) <= b < ((3*n)+3):

                if a==(3*m):
                    rule1=l[a+1][b] != '' and k in l[a+2]
                    rule2=l[a+2][b] !=''  and k in l[a+1]
                    return rule1 or rule2
                elif a==((3*m)+2):
                    rule1=l[a-1][b] != '' and k in l[a-2]
                    rule2=l[a-2][b] != ''and k in l[a-1]
                    return rule1 or rule2
                else:
                    rule1=l[a-1][b] != '' and k in l[a+1]
                    rule2=l[a+1][b] != '' and k in l[a-1]
                    return rule1 or rule2
    
