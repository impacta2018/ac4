from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path ('', index),
    path ('contato/', contato),
    path ('login/', login),
	path('admin/', admin.site.urls),
]
