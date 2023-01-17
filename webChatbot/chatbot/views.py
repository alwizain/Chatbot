from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Respon, Responses
from chatbot.forms import ResponCreateForm, ResponsesCreateForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def index(request):
  data = Respon.objects.all()
  paginator = Paginator(data, 15) # Show 25 contacts per page.
  page = request.GET.get('page')
  page_res = paginator.get_page(page)
  
  form = ResponCreateForm(request.POST)
  if request.method == 'POST':
    form = ResponCreateForm(request.POST)

    if form.is_valid():
      form.save(commit=True)
      return redirect('../chatbot')
    else:
      print("error")


  context = {
	'subjudul' : "Manage Input Chatbot",
  'data' : data,
  'page_res' : page_res,
  'form' : form,
  }
  
  return render(request,'chatbot/index.html',context)


@login_required(login_url='/login')
def indexresp(request):
  data = Responses.objects.all()
  paginator = Paginator(data, 10) # Show 25 contacts per page.
  page = request.GET.get('page')
  page_res = paginator.get_page(page)
  
  form = ResponsesCreateForm()
  if request.method == 'POST':
    form = ResponsesCreateForm(request.POST)

    if form.is_valid():
      form.save(commit=True)
      return redirect('../chatbot/res')
    else:
      print("error")


  context = {
	'subjudul' : "Manage Respon Chatbot",
  'dataresp' : data,
  'page_res' : page_res,
  'formresp' : form,
  }
  
  return render(request,'chatbot/indexresp.html',context)

@login_required(login_url='/login')
def updateresp(request, id):
  updtresp = get_object_or_404(Responses, id=id)
  dataresp = Responses.objects.all()

  dt = {
    'tag' : updtresp.tag,
    'responses' : updtresp.responses,
  }

  form = ResponsesCreateForm(request.POST or None, instance=updtresp)
  if request.method == 'POST':
    if form.is_valid():
      form.save()
    return redirect('chatbotresp')
    

  context = {
	'subjudul' : "Manage Chatbot",
  'data' : dataresp,
  'form' : form,
  }
    
  return render(request,'chatbot/update_viewresp.html',context)

@login_required(login_url='/login')
def update(request, id):
  updt = get_object_or_404(Respon, id=id)
  data = Respon.objects.all()

  dt = {
    'tag' : updt.tag,
    'patterns' : updt.patterns,
  }

  form = ResponCreateForm(request.POST or None, instance=updt)
  if request.method == 'POST':
    if form.is_valid():
      form.save()
    return redirect('chatbot')
    

  context = {
	'subjudul' : "Manage Chatbot",
  'data' : data,
  'form' : form,
  }
    
  return render(request,'chatbot/update_view.html',context)

@login_required(login_url='/login')
def delete(request, id):
  delt = Respon.objects.get(id=id)
  delt.delete()
  return redirect('chatbot')

@login_required(login_url='/login')
def deleteresp(request, id):
  delt = Responses.objects.get(id=id)
  delt.delete()
  return redirect('chatbotresp')
