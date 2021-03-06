"""secondproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,include,url
from django.contrib import admin
from myapp.views import index,register,walkin,calling,counselling,joining,currentstatus
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',index,name="index"),
    url(r'^register$',register,name="register"),
    url(r'^walkin$',walkin,name="walkin"),
    url(r'^calling$',calling,name="calling"),
    url(r'^counselling$',counselling,name="counselling"),
    url(r'^joining$',joining,name="joining"),
    url(r'^currentstatus$',currentstatus,name="currentstatus"),


    url(r'^myapp/', include('myapp.urls'))
    

]
