from django.conf.urls import url
from .views import chat_view, index_view

urlpatterns = [
    url(r'chat/$', chat_view, name='chat'),
    url(r'index/$', index_view, name='index'),
]
