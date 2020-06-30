from django.contrib import admin  
from django.urls import path ,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [  
    path('',include('perfiles.urls')),  
    path('dashboard/reportes/',include('reportes.urls')), 
    path('dashboard/departamentos/',include('departamentos.urls')), 
    path('dashboard/municipios/',include('municipios.urls')), 
    path('admin/', admin.site.urls), 
    #path('accounts/',include('accounts.urls')) 
]  

urlpatterns += staticfiles_urlpatterns()