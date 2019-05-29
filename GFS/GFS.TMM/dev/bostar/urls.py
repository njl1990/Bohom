from django.contrib import admin
from django.urls import include, path

urlpatterns = [
	path('tmm/',include('tmm.urls')),
]