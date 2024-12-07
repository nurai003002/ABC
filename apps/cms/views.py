from django.shortcuts import render

from apps.settings.models import Setting
# Create your views here.

def coming_soon(request):
    setting = Setting.objects.latest('id')
    return render(request, 'coming-soon.html', locals())

def pricing(request):
    setting = Setting.objects.latest('id')
    return render(request, 'pricing.html', locals())