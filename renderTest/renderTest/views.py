from django.shortcuts import render, redirect

from .models import TestItem
# Create your views here.

def index(request):
    listItems = TestItem.objects.all()
    trues = TestItem.objects.filter(flag = True)
    falses = TestItem.objects.filter(flag = False)
    context = {
        'listItems': listItems,
        'trues': trues,
        'falses': falses,
    }
    return render(request, 'renderTest/index.html', context)

def addItem(request):
    if(request.method == 'POST'):
        newItem = request.POST.get('newItem')
        item = TestItem.objects.create(name = newItem)
    return redirect('/')

def markTrue(request):
    if(request.method == 'POST'):
        item = request.POST.get('item')
        currentItem:TestItem = TestItem.objects.filter(name = item).first()
        print(currentItem)
        currentItem.flag = True
        currentItem.save()
    return redirect('/')