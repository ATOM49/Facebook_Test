from django.conf.urls import patterns, include, url

from Facebook import views

urlpatterns = patterns('',
	url(r'^$', views.IndexView, name='index'),
	)