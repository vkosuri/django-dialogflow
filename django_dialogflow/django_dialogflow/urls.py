from django.conf.urls import include, url
from django.contrib import admin
from .views import chat_view, index_view

urlpatterns = [
    url(r'chat/$', chat_view, name='chat'),
    url(r'index/$', index_view, name='index'),
    url(r'^admin/', admin.site.urls),
]
