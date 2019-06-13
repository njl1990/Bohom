from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from django.template import loader
from bson.objectid import ObjectId
from bson import json_util
from glm.service import GlmService

def Index(request):
        imageList=[]
        imageList.append('image-1.jpg')
        imageList.append('image-2.jpg')
        imageList.append('image-3.jpg')
        imageList.append('image-4.jpg')
        imageList.append('image-5.jpg')
        imageList.append('image-6.jpg')
        context = { 'imageList':imageList }
        return render(request, 'Overview.html', context)

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