from django.shortcuts import render



# Create your views here.
def listfunc(request):
    return render(request,'sample/post_list.html')
    