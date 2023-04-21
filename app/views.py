from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from app.models import *
# Create your views here.
def Topics(request):
    TFO=TopicForm()
    d={'TFO':TFO}
    if request.method=='POST':
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            topic_name=TFD.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=topic_name)[0]
            TO.save()
            #return HttpResponse('Topic inserted....')
            TQS=Topic.objects.all()
            d={'TQS':TQS}
            return render(request,'display_topic.html',d)
    return render(request,'insert_topic.html',d)

def Webpage(request):
    WFO=WebpageForm()
    d={'WFO':WFO}
    return render(request,'insert_webpage.html',d)
