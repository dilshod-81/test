"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path
from main.views import main_index, main_add_sinf, main_add_dars, main_dars_jadval



urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    path('', main_index, name = "main_index"),
    path('add/sinf/', main_add_sinf, name = "main_add_sinf"),
    path('add/dars/', main_add_dars, name = "main_add_dars"),
    path('jadval/<int:sinf_id>/', main_dars_jadval, name="dars-jadval")

)


