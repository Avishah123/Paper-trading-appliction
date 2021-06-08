from django.core.checks import messages
from django.shortcuts import redirect, render
import requests
import json

from django.contrib import messages

from .forms import *
from .models import *

# key = pk_5a0da994dbda4257ad0a706da01d5ca0
# Create your views here.

def home(request):

    

    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_request = requests.get('https://cloud.iexapis.com/stable/stock/'+ticker+'/quote?token=pk_aac6e9de20cf4b69b985ac74d6524493')
        try:
            api = json.loads(api_request.content)

        except Exception as e :
            api = "error .."
        
        return render(request,'index.html', {'api' : api})

    else :
        return render(request,'index.html', {'ticker' : "Enter a ticker symbol above"})


    
def add_stock(request):

    def cut(value):
        return value*1000
    

    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request,("stock has been added succesfully"))
            return redirect('add_stock')
    
    else :
        ticker = Stock.objects.all()
        output = []
        for ticker_item in ticker :
            api_request = requests.get('https://cloud.iexapis.com/stable/stock/'+str(ticker_item)+'/quote?token=pk_aac6e9de20cf4b69b985ac74d6524493')
            try:
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e :
                api = "error .."
        
        
        
        
        
        return render(request,'add_stock.html',{'ticker' : ticker,'output' : output})
    

def about(request):
    return render(request,'about.html',{})

def delete(request,stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request,("stock has been removed succesfully"))
    return redirect('add_stock')

def delete_stock(request):
    ticker = Stock.objects.all()
    return render(request,'delete_stock.html',{'ticker' : ticker})

def testing(request):
    return render(request,'testing.html',{})