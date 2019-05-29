from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from django.template import loader
from bson.objectid import ObjectId
from bson import json_util


def TmInfo(request):
	context = {}
	##print(context)
	return render(request, 'TmmInfo.html', context)
	
def LoadTmData(request):
	
	x=[1,2,3]
	y=[4,5,6]
	context = {
		'x':x,
		'y':y,}
	return HttpResponse(json_util.dumps(context))