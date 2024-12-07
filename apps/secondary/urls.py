from django.urls import path

from apps.secondary import views

urlpatterns = [
    # blog
    path('blog/', views.blog, name='blog'),
    path('blog-detail/', views.blog_detail, name='blog_detail'),
    # study_case
    path('study-case/', views.study_case, name='study_case'),
    path('study-case-detail/', views.study_case_detail, name='study_case_detail'),
    # services
    path('services/', views.services, name='services'),
    path('service-detail/', views.service_detail, name='service_detail'),
    # team
    path('team/', views.team, name='team'),
    path('team-detail/', views.team_detail, name='team_detail'),
]