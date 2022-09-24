from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.search, name='home'),
    path('result/',views.result, name='result'),
]
