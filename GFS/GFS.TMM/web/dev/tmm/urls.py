from django.urls import path
from . import views

urlpatterns = [
    path('', views.TmInfo, name='TmInfo'),
	path('TmInfo', views.TmInfo, name='TmInfo'),

	# API
	## Load 
	path('LoadTmData', views.LoadTmData, name='LoadTmData'),
	
]