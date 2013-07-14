from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shopaholic.views.home', name='home'),
    # url(r'^shopaholic/', include('shopaholic.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^parse-jabong/', 'html_parser.views.parse_jabong', name='parse_jabong'),
)

urlpatterns += patterns('',
                        url(r'^/?$', 'dashboard.views.dashboard'),
                        url(r'^product/(?P<slug>.+?)/?$','dashboard.views.product_page')
)
