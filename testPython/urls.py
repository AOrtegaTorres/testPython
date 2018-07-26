
from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('', include('random_number.urls', namespace='numbers')),
    path('admin/', admin.site.urls),
]
