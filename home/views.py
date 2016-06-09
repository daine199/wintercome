from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings


# Create your views here.


def index(request):
    if request.method == 'GET':
        return render(request, 'home/index.html')
    if request.method == 'POST':
        app_name = request.POST.get('app_name')
        if app_name in settings.INSTALLED_APPS:
            return redirect("/" + app_name)
        else:
            context = {"error": "Invalid App"}
            return render(request, 'home/index.html', context)
