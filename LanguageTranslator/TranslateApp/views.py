from django.shortcuts import render

# Create your views here.
def Translate(request):
    data=request.POST['text']
    context={
        'datas':data
    }

    return render(request,'translate.html',context)
