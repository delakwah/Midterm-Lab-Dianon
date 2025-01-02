from django.shortcuts import render, get_object_or_404, redirect
from .forms import LostItemForm
from .models import LostItem


# Create your views here.

def index(request):
    return render(request, "index.html")

def report(request):
    if request.method == 'POST':
        form = LostItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('items')
    else:
        form = LostItemForm()
    return render(request, 'report.html', {'form': form})

def items(request):
    items = LostItem.objects.all()
    return render(request, 'items.html', {'items': items})

def detail(request, pk):
    item = get_object_or_404(LostItem, pk=pk)
    return render(request, 'detail.html', {'item': item})

def delete(request, pk):
    item = get_object_or_404(LostItem, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('items')
    return render(request, 'delete.html', {'object': item})

def update(request, pk):
    item = get_object_or_404(LostItem, pk=pk)

    if request.method == 'POST':
        form = LostItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()  # Save the updated item
            return redirect('items')  # Redirect to the list view
    else:
        form = LostItemForm(instance=item)  # Populate the form with existing item data

    return render(request, 'update.html', {'form': form, 'item': item})

