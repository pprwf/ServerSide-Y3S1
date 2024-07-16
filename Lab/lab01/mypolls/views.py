from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Question as q

def index(request):
    latest = q.objects.order_by("-date")[:10]
    return render(request, "index.html", {"latest": latest})

def detail(request, id):
    try:
        qid = q.objects.get(pk = id)
    except q.DoesNotExist:
        raise Http404("Question not found")
    return render(request, "detail.html", {"qid": qid})

def results(request, id):
    return HttpResponse("This is an answer of a Q" + id)

def vote(request, id):
    return HttpResponse("You're voting on Q", id)
