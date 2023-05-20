from django.shortcuts import render, get_object_or_404,redirect
from .models import Item # . is used since on the same folder 
from  django.contrib.auth.decorators import login_required # to makesure user logged in


from .forms import NewItemForm,EditItemForm

# Create your views here.


def detail(request,pk): #since we want to know the detail of specific item, we need a id/pk
    item = get_object_or_404(Item, pk=pk) # first pk on the model itlsel
                                            #second pk is for the one we get fromthe url
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
#get all items in the same category and filter out if sold and exlude it from the list
    return render(request, 'item/details.html', {
        'item':item,
        'related_items': related_items
    })
    

@login_required #if logged in then access this method 
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm() # create NewItemForm
    
    return render(request, 'item/form.html', {
        'form' : form ,   #  pass in the form 
        'title': 'New Item', # this will go to the title of the forms.html
      })
    
@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk,created_by=request.user)
    item.delete()
    return  redirect('dashboard:index')

def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            # Save the form and redirect
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail', pk=item.id)
        else:
            # Print form errors
            print(form.errors)
    else:
        form = EditItemForm(instance=item)
    
    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit Item',
    })
    
def items(request):
    query = request.GET.get('query', '')
    items = Item.objects.filter(is_sold=False)
    
    if query: #if there the any query
        items = items.filter(name__icontains=query) #if name contains any query (insensitive)
    
    return  render(request, 'item/items.html',{
        'items': items,
        'query': query,
        
    })