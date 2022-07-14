from .forms import FeedingForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Cat


# Faux Cat Data - Database simulation

# class Cat:
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age
    
# cats = [
#     Cat('Lolo', 'tabby', 'foul little demon', 3),
#     Cat('Ryder', 'golden', 'pain in my butt', 0),
#     Cat('Raven', 'black tabby', 'likes tuna', 4)
# ]
    
# Create your views here.

def home(request):
    return HttpResponse('<h1> Hello World</h>')


def about(request):
#Sendoing back Raw Text or HTML String
#httpresponse
#return HttpResponse ("About Page")
#sending back a full template file
 return render(request, "about.html")

def cats_index(request):
    cats = Cat.objects.all()
    return render(request, "cats/index.html", {'cats' :cats})


def cats_detail(request, cat_id):
  ## Get the the individual cat
  cat = Cat.objects.get(id=cat_id)
  #INSTANTIATE OUR FEEDING FORM
  feeding_form = FeedingForm()
  ## render template, pass it the cat
  return render(request, 'cats/detail.html', { 'cat': cat, 'feeding_form':feeding_form})

def add_feeding(request, cat_id):
  #Create the model form using the request.POST
  form = FeedingForm(request.POST)
  #Validate form
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.cat_id = cat_id
    new_feeding.save()
  return redirect('detail', cat_id=cat_id)
    
    
class CatCreate(CreateView):
    model = Cat
    fields = "__all__"
    success_url = '/cats/'

class CatUpdate(UpdateView):
  model = Cat
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['breed', 'description', 'age']

class CatDelete(DeleteView):
  model = Cat
  success_url = '/cats/'


