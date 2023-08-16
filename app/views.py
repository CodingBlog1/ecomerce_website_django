from django.shortcuts import render
from django.views import View
from store.models import Product 
# Create your views here.

class Home(View):
    def get(self,request):
        product = Product.objects.all().filter(is_available = True)
        return render(request,'index.html',{'products':product})