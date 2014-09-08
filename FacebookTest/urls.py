from django.conf.urls import patterns, include, url

from django.contrib import admin
from Facebook import urls
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'FacebookTest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^facebook/', include('django_facebook.urls')),
    url(r'^test/', include('Facebook.urls', namespace = "test")),

)