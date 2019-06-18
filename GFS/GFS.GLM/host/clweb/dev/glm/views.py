from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from django.template import loader
from bson.objectid import ObjectId
from bson import json_util
from glm.service import GlmService

def Index(request):
        imageList=[]
        imageList=GlmService.LoadDbData()
        context = { 'imageList':imageList }
        return render(request, 'Overview.html', context)


def List(request):
        imageList=[{'date':'2019-03-4','num':'32'},]
        #imageList=GlmService.LoadDbData()
        context = { 'imageList':imageList }
        return render(request, 'List.html', context)

'''
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
'''