from django.conf.urls import patterns, include, url
from django.contrib import admin
from views.views import index, location, merch, performances, tickets
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'main.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
    url(r'^location', location),
    url(r'^merch', merch),
    url(r'^performances', performances),
    url(r'^tickets', tickets),
)
