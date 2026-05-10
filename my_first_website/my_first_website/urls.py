from django.contrib import admin
from django.urls import path
from basic_app import views # استيراد الـ view اللي عملناه

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'), # الصفحة الرئيسية
]