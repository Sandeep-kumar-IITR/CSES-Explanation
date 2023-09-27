from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render


# from topic.models import topic
from main.models import topic , question

def home(request):

    if request.method == "GET":
        topic_names = topic.objects.all()
        data = {
                    'topic_names':topic_names,
                    
                }
        return render(request , "index.html",data)
    

    if request.method=='POST':
        n1 = request.POST.get('topic_name')
        tpn ={
          'val':n1
        }
        url  = "/topic_form/?output={}".format(n1)
        return HttpResponseRedirect(url)


    

def topic_form(request):
    
    if request.method=="GET":
        topic_name = int(request.GET.get('output'))

        data = question.objects.all().filter(topic=topic_name)
        return render(request , "topic_name.html",{"output":data})
    
    if request.method=='POST':
        n1 = request.POST.get('question_name')
        tpn ={
            'val':n1
        }
        url  = "/question_form/?output={}".format(n1)
        return HttpResponseRedirect(url)
    return render(request , "question_name.html")






def question_form(request):
    
    if request.method=="GET":
        question_name = request.GET.get('output')
        data = question.objects.all().filter(question_name=question_name).values()
        return render(request , "question_name.html",data[0])
    
    # if request.method=='POST':
    #     n1 = request.POST.get('question_name')
    #     tpn ={
    #         'val':n1
    #     }
    #     url  = "/topic_form/?output={}".format(n1)
    #     return HttpResponseRedirect(url)
    # return render(request , "question_name.html")

