from django.shortcuts import render

from apps.settings.models import Setting    
# Create your views here.

def blog(request):
    setting = Setting.objects.latest('id')
    return render(request, 'blogs/blog.html', locals())

def blog_detail(request):
    setting = Setting.objects.latest('id')
    return render(request, 'blogs/blog-details.html', locals())

def study_case(request):
    setting = Setting.objects.latest('id')
    return render(request, 'study_case/case-study.html', locals())

def study_case_detail(request):
    setting = Setting.objects.latest('id')
    return render(request, 'study_case/case-study-details.html', locals())

def services(request):
    setting = Setting.objects.latest('id')
    return render(request, 'services/services.html', locals())

def service_detail(request):
    setting = Setting.objects.latest('id')
    return render(request, 'services/service-detail.html', locals())

def team(request):
    setting = Setting.objects.latest('id')
    return render(request, 'team/team.html', locals())

def team_detail(request):
    setting = Setting.objects.latest('id')
    return render(request, 'team/team-detail.html', locals())

