def boxfill(k,l,a,b):
    if l[a].count('')==2 and k not in l[a]:
        return True
    elif [l[s][a] for s in range(0,9)].count('')==2 and k not in [l[s][a] for s in range(0,9)]:
        return True
    else: return False
        
    
