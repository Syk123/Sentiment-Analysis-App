from django.shortcuts import render
from django.views.generic import TemplateView
from twitterStream import sentiment_analysis
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def stats(request):
    if request.method == 'POST':
        search_val = request.POST.get("handle",None)
        (per_pos,per_neg,per_neut) = sentiment_analysis(search_val)
        return render(request,'stats.html',{'search':search_val, 'pos':per_pos,'neg': per_neg, 'neut': per_neut})
    return render(request,'index.html')
