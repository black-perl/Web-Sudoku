from django.http import HttpResponse,HttpRequest
from django.template import RequestContext,loader
from django.shortcuts import render_to_response
from sudoku_solver import sudoku1


def fill(request):
    l=[[""]*9]*9#defining empty one
    if request.method=="POST":#or you can use bool(request.POST) as empty dict
        enteries=request.POST.getlist('enteries')
        enteries=beautify(map(str,enteries))
        l=sudoku1.solve(enteries,3)
        print l
        return render_to_response("django-template.html",{"grid":reverse_beautify(l)},RequestContext(request))
    else:
        return render_to_response("django-template.html",{"grid":l},RequestContext(request))

def beautify(l):
    new=[]
    for i in range(3):
      for k in range(3) :
        new.append(l[(3*k+27*i):(3*k+27*i+3)]+l[(3*k+27*i+9):(3*k+27*i+12)]+l[(3*k+27*i+18):(3*k+27*i+21)])

    return new


def reverse_beautify(l):
    m=[]
    for k in l:
        m=m+k
    new=[]
    for i in range(3):
        for k in range(3):
            new.append(m[(3*k+27*i):(3*k+27*i+3)]+m[(3*k+27*i+9):(3*k+27*i+12)]+m[(3*k+27*i+18):(3*k+27*i+21)])
    return new



