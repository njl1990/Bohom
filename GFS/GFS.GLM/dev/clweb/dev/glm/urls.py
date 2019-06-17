from django.urls import path
from . import views

urlpatterns = [
    path('', views.List, name='List'),
	path('overview', views.Index, name='Index'),
	path('list', views.List, name='List'),
]