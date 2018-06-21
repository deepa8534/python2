from django.conf.urls import patterns, include, url
from .views import register,index,walkin,calling,counselling,joining,currentstatus
urlpatterns = patterns('',url(r'^index/', index, name = 'index')
	,url(r'^register/',register,name='register'),
	url(r'^walkin/',walkin,name='walkin'),
	url(r'^calling/',calling,name='calling'),
	url(r'^counselling/',counselling,name='counselling'),
	url(r'^joining/',joining,name='joining'),
	url(r'^currentstatus/',currentstatus,name='currentstatus'))