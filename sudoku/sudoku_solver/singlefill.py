def colfill(k,l,a,b):
    lis=[l[s][b] for s in range(0,9)]
    return lis.count('')==1 and k not in lis

def rowfill(k,l,a,b):
    lis=l[a]
    return lis.count('')==1 and k not in lis
