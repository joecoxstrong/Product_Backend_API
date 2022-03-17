from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    path('', views.ReviewList),
    path('<int:fk>/', views.ReviewDetail),
    path('reviews<int:fk>/', views.ReviewDetail)
]    

urlpatterns = format_suffix_patterns(urlpatterns)