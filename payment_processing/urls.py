from django.conf.urls import patterns, include, url
from django.contrib import admin
from djang.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'profiles.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^anotherurlpattern/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)