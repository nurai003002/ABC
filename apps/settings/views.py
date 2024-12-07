from django.shortcuts import render

from apps.settings.models import Setting
# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    return render(request, 'base/index.html', locals())

def contact(request):
    setting = Setting.objects.latest('id')
    return render(request, 'base/contact.html', locals())

def about(request):
    setting = Setting.objects.latest('id')
    return render(request, 'base/about.html', locals())

