from django.shortcuts import render
from .forms import AddPhoneForm
from django.http import HttpResponse

#from .models import Phone
# Create your views here.
def add_phone(request):
    if request.method == "GET":
        form = AddPhoneForm()
        return render(request, 'example.html', {'form': form})
    if request.method == "POST":
        phone = AddPhoneForm(request.POST)
        if form.is_valid():
            phone = form.save()
            return HttpResponse('Done!', status=201)    
        return HttpResponse('Error', status=400)
    #we can write this  CreateAPIView
    
    
