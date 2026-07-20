from django.shortcuts import render

# Create your views here.
# <<<<<<< HEAD
# =======
def home(req):
    return render(req, 'home.html')

def base(req):
    return render(req, 'base.html')

def c1(req):
    return render(req, 'docs/chap1.html',{
        "page" : "c1"
    })

def c2(req):
    return render(req, 'docs/chap2.html',{
        "page" : "c2"
    })

def c3(req):
    return render(req, 'docs/chap3.html',{
        "page" : "c3"
    })

def c4(req):
    return render(req, 'docs/chap4.html',{
        "page" : "c4"
    })

def c5(req):
    return render(req, 'docs/chap5.html',{
        "page" : "c5"
    })

def c6(req):
    return render(req, 'docs/chap6.html',{
        "page" : "c6"
    })

# >>>>>>> feature/documents
