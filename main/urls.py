from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView.as_view(url='base')),
    path('donateppe', views.MainView.as_view(url='donateppe'))
]