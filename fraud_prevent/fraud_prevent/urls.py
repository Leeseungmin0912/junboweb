from django.contrib import admin
from django.urls import path
from checker import views

urlpatterns = [
    path('admin/', admin.site.urls),  # right를 urls로 수정!
    path('', views.index),
]