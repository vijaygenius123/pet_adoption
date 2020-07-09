from django.contrib import admin
from django.urls import path

from adoptions.views import home, pet_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('adoptions/<int:pet_id>/', pet_detail,name='pet_detail'),
]
