"""oracle_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from clothes import views
from clothes.views import index_view, statistics
from clothes.views import about
from clothes.views import brilliant
from clothes.views import collection
from clothes.views import delivery
from clothes.views import jewellery
from clothes.views import order
from clothes.views import premium
from clothes.views import present
from clothes.views import wedding
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index_view),
    path('about/',about),
    path('brilliant/', brilliant),
    path('collection/', collection),
    path('delivery/', delivery),
    path('jewellery/', jewellery),
    path('order/', order),
    path('premium/', premium),
    path('present/', present),
    path('wedding/', wedding),
    path('statistics/', statistics)
    # path('stats/', views.stat, name="stat")

]

