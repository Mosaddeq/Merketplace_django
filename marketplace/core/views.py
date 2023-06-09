from django.shortcuts import render, redirect
from django.http import JsonResponse

from django.contrib.auth import logout

from item.models import Category, Item

from .forms import SignupForm
# Create your views here.

def index(request):
    items = Item.objects.filter(is_sold = False)[0:6]
    categories= Category.objects.all()
    return render(request, 'core/index.html' , {
              'categories': categories,
              'items' : items,

        })


def api_index(request):
    items = list(Item.objects.filter(is_sold=False).values())
    categories = list(Category.objects.values())
    return JsonResponse({
        'categories': categories,
        'items': items,
    })

def contact(request):
        return render(request, 'core/contact.html' ) 


def signup(request):
      if request.method == 'POST': # to knwo if for submitted
            form = SignupForm(request.POST) # to get the data from form
            if form.is_valid(): #check  if valid
                  form.save()

                  return redirect('/login') #import redirect to use redirect
      form = SignupForm()

      return render(request, 'core/signup.html', {
        'form': form,
      })
def logout_view(request):
    logout(request)
    return redirect('core:index')