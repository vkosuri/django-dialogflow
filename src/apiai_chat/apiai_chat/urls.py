from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('chat.urls', namespace='apiai')),
    url(r'^admin/', admin.site.urls),
]
