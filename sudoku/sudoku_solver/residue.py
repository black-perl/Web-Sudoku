#tell the no. of numbers remaining to be filled in a matrix square
def toFill(s):
    test=['1','2','3','4','5','6','7','8','9']
    residue=[]
    for dummy in test:
        if dummy not in s:
            residue.append(dummy)
        else:
            pass

    return residue

        
