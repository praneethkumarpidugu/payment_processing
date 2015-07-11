from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'payment_processing.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^anotherurlpattern/', include(admin.site.urls)),
)
