#single value check for row
def single_row(l,a,b):
    for m in range(3):
        for n in range(3):
            if (3*m) <= a < ((3*m)+3) and (3*n) <= b < ((3*n)+3):

                if a==(3*m):
                    rule1=l[a+1][b] != ''
                    rule2=l[a+2][b] !=''
                    return rule1 and rule2
                elif a==((3*m)+2):
                    rule1=l[a-1][b] != ''
                    rule2=l[a-2][b] != ''
                    return rule1 and rule2
                else:
                    rule1=l[a-1][b] != ''
                    rule2=l[a+1][b] != ''
                    return rule1 and rule2
    
    
