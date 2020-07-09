from django.shortcuts import render

def index(request):
    return render(request,'core/index.html')

def pagetype_template(request):
    path=request.path
    path=path.split("/")
    return render(request,'core/'+path[2]+'page.html')



