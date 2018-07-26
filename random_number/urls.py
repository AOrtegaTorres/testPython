from django.urls import path
from django.conf.urls import url
from random_number import views

from .views import (
    NumberList,
    NumberDetail,
    NumberUpdate,
    NumberDelete
)
app_name = "numbers"

urlpatterns = [
    url(r'^$', NumberList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', NumberDetail.as_view(), name='detail'),
    url(r'^guardar$', views.save, name='new'),
    url(r'^editar/(?P<pk>\d+)$', NumberUpdate.as_view(), name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', NumberDelete.as_view(), name='delete'),
]
