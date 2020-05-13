from django.shortcuts import render, redirect, get_object_or_404 
from django.http import HttpResponseRedirect , HttpResponse
from django.template import loader
from .forms import StuForm
from .models import Student



def index(request):
  return render(request,'home.html')

def data(request):
  data=Student.objects.all()
  context={
   'data':data,
   }
  return render(request,'data.html',context)  

def intex(request):
  form=StuForm()
  context={
   'form':form,
   }
  if request.method== 'POST':
   form=StuForm(request.POST,request.FILES)
   if form.is_valid:
    form.save()
    return HttpResponseRedirect('/admin/')
  else:
   form=StuForm() 
  return render(request,"index.html",context)


  
def update(request, id):
  obj=get_object_or_404(Student, id=id)
  if request.method=="POST":
    form= StuForm(request.POST, request.FILES, instance=obj)
    if form.is_valid:
      form.save()
      return redirect('/data/')
  else:
    form = StuForm(instance=obj)    
  return render(request,"update.html",{'form':form})  

def delete(request,id):
  context={}
  obj=get_object_or_404(Student,id=id)
  if request.method=="POST":
    obj.delete()
    return HttpResponseRedirect("/data/")
  return render(request,"delete.html",context)

def item(request,id):
 context={
  'data':Student.objects.get(id=id)
 }
 return render(request,"item.html",context)
 

