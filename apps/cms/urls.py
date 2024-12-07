from django.urls import path

from apps.cms.views import coming_soon, pricing

urlpatterns = [
    path('coming-soon/', coming_soon, name='coming_soon'),
    path('pricing/', pricing, name='pricing'),
]