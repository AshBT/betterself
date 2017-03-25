from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views import defaults as default_views
from django.views.generic import TemplateView
from rest_framework.authtoken import views

urlpatterns = [
    # General
    url(r'^$', TemplateView.as_view(template_name='pages/home/index.html'), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),
    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, include(admin.site.urls)),
    # User Management
    url(r'^users/', include('betterself.users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),
    # API
    url(r'^api/', include('apis.urls')),
    url(r'^analytics/', include('analytics.urls')),
    url(r'^react/$', TemplateView.as_view(template_name='react.html'), name='react'),
    # curl -X POST -d "username=SOMETHING&password=SOMEPASSWORD" localhost:9000/api-token-auth/
    url(r'^api-token-auth/', views.obtain_auth_token, name='api_token'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),

    ]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
