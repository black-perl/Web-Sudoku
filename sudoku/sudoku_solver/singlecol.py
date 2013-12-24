#single value check for column
def single_col(l,a,b):
    for n in range(3):
        for m in range(3):
            if (3*m) <= a < ((3*m)+3) and (3*n) <= b < ((3*n)+3):

                if b==(3*n):
                    rule1=l[a][b+1] != ''
                    rule2=l[a][b+2] !=''
                    return rule1 and rule2
                elif b==((3*n)+2):
                    rule1=l[a][b-1] != ''
                    rule2=l[a][b-2] != ''
                    return rule1 and rule2
                else:
                    rule1=l[a][b-1] != ''
                    rule2=l[a][b+1] != ''
                    return rule1 and rule2
    
    
