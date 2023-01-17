from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from chatbot.models import Respon, Responses

def search(request):
    search = request.GET.get('q')
    data = Respon.objects.all()

    if search:
        data = data.filter(
            Q(patterns__icontains=search)|Q(tag__icontains=search)
        )

    
    
    context = {
        "subjudul":"Pencarian",
        "data": data,
        "search": search,
    }
    
    return render(request, 'chatbot/index.html', context)

def searchr(request):
    searchr = request.GET.get('j')
    page_res = Responses.objects.all()

    if searchr:
        page_res = page_res.filter(
            Q(tag__icontains=searchr)
        )

    
    
    context = {
        "subjudul":"Pencarian",
        "page_res": page_res,
        "searchr": searchr,
    }
    
    return render(request, 'chatbot/indexresp.html', context)