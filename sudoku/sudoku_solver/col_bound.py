def col_bound(k,l,a,b):
    for n in range(3):
        for m in range(3):
            if (3*m) <= a < ((3*m)+3) and (3*n) <= b < ((3*n)+3):

                if b==(3*n):
                    bool1= l[a][b+1] != '' and k in [l[s][b+2] for s in range(0,9)]
                    bool2= k in [l[s][b+1] for s in range(0,9)] and l[a][b+2] !=''
                    return bool1 or bool2    
            
                        
                elif b==((3*n)+2):
                    bool1= l[a][b-1] != '' and k in [l[s][b-2] for s in range(0,9)]
                    bool2= k in [l[s][b-1] for s in range(0,9)] and l[a][b-2] != ''
                    return bool1 or bool2
                   
                else:
                    bool1= k in [l[s][b+1] for s in range(0,9)] and l[a][b-1] != ''
                    bool2= k in [l[s][b-1] for s in range(0,9)] and l[a][b+1] != ''
                    return bool1 or bool2
                     
