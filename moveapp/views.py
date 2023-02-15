from django.shortcuts import render
from .models import Add
from .forms import AddForm
# Create your views here.
def about(request):
  return render(request,'pages/about.html')

def home(request):
  context = {
    'move' : Add.objects.all(),
  }
  return render(request,'pages/home.html',context)


def add(request):
  if request.method == 'POST':
    add_move = AddForm(request.POST,request.FILES)
    if add_move.is_valid():
      print('hello')
      add_move.save()

  context = {
    'form' : AddForm(),
  }
  return render(request,'pages/add.html',context)
