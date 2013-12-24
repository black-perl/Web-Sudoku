from checker import *
from colcheck import col_check
from residuefill import residueFill
from rowcheck import row_check
from singlecol import single_col
from singlerow import single_row
from residue import toFill
from test_box import test_box
from rowbound import row_bound
from col_bound import col_bound
from singlefill import *
from fill1 import colrow
from boxfill import boxfill


def solve(l,a):
    test=['1','2','3','4','5','6','7','8','9']
    l,a=empty_check(l,a)
    while len(a)!=0:
     #for mat in pack(l):
        #for k in toFill(mat):
           
         for k in test:
             for c in a:
                
                if single_row(l,c[0],c[1]) and col_check(k,l,c[0],c[1]) and test_box(l,c[0],c[1],len(l),k):
                   l[c[0]][c[1]]=k
                   a.remove(c)
                   print '.'
                   
                

                elif single_col(l,c[0],c[1]) and row_check(k,l,c[0],c[1]) and test_box(l,c[0],c[1],len(l),k):
                    l[c[0]][c[1]]=k
                    a.remove(c)
                    print "."
                    
                    
                

                elif row_bound(k,l,c[0],c[1]) and col_check(k,l,c[0],c[1]) and test_box(l,c[0],c[1],len(l),k):
                   l[c[0]][c[1]]=k
                   a.remove(c)
                   print '.'
                   
                   

                elif col_bound(k,l,c[0],c[1]) and row_check(k,l,c[0],c[1]) and test_box(l,c[0],c[1],len(l),k):
                    l[c[0]][c[1]]=k
                    a.remove(c)
                    print '.'
                    
                    
                elif  col_check(k,l,c[0],c[1])  and row_check(k,l,c[0],c[1]) and test_box(l,c[0],c[1],len(l),k):
                    l[c[0]][c[1]]=k
                    a.remove(c)
                    print '.'
                    
                    
       
                elif colfill(k,l,c[0],c[1]) or rowfill(k,l,c[0],c[1]):
                    l[c[0]][c[1]]=k
                    a.remove(c)
                    print '.'
                    
                    
                    
                elif colrow(k,l,c[0],c[1]):
                    a.remove(c)
                    l[c[0]][c[1]]=k
                    print '.'
                    

                elif boxfill(k,l,c[0],c[1]) and test_box(l,c[0],c[1],len(l),k):
                    a.remove(c)
                    l[c[0]][c[1]]=k
                    print '.'
                    

            
                    
       

                else:pass

                   
    return l



