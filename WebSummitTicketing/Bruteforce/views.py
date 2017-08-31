from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render


def home(request):

    return render(request,'index.html')


def ajax(request):

    

    code=request.GET.get('code',None)

    print(code)

    if code=="LWFD1234m":
        data = {
            'sucess': 'available'
        }
    else:
        data={
        'success':'unavailable'
        }
    
    return JsonResponse(data)



