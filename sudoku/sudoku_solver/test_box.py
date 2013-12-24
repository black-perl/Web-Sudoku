from checker import *
def test_box(l,a,b,len1,k):
    if a<3 :
       if b<3:
           return k not in pack(l)[0]
       elif b<6:
           return k not in pack(l)[1]
       else:
            return k not in pack(l)[2]
    elif  3 <= a <6:
       if b<3:
           return k not in pack(l)[3]
       elif b<6:
           return k not in pack(l)[4]
       else:
            return k not in pack(l)[5]
    else:
       if b<3:
           return k not in pack(l)[6]
       elif b<6:
           return k not in pack(l)[7]
       else:
           return k not in pack(l)[8]
