from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
   path('',views.login,name='login'),
   path('admin/', admin.site.urls),
   path('login', admin.site.urls)

]