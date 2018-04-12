from django.conf.urls import include, url
from fileclassifier import views

urlpatterns = [
    url(r'^$', views.base_view), #base url
    url(r'^get_response$', views.get_response, name='get_response'), #process request url
]
