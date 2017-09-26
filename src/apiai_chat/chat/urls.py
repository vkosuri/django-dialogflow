from django.conf.urls import url
from .views import ApiAiView

urlpatterns = [
    url(r'^$', ApiAiView.as_view(), name='main'),
]
