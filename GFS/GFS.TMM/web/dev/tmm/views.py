from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from django.template import loader
from bson.objectid import ObjectId
from bson import json_util
import tmm.service


def TmInfo(request):
    context = {'name':'name'}
    print(context)
    return render(request, 'TmmInfo.html', context)
	
def LoadTmData(request):
    print('LoadTmmData')
    tmmRcdList=TmmService.LoadTmData()
    print('ok')
    x=[]
    y=[]
    for item in tmmRcdList:
        x.append(item['time'])
        y.append(item['tmp'])
    context={'x':x,'y':y,}
    return HttpResponse(json_util.dumps(context))
