from django.shortcuts import render
from .forms import AddPhoneForm
from django.http import HttpResponse
import json
from .reports import all_brands_in_korea, some_brand_mobiles, mobiles_brand_nation_equals_made_in 
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
    
    
def report(request):
    response_data = {}
    response_data['all_brands_in_korea'] = all_brands_in_korea()
    response_data['some_brand_mobiles'] = some_brand_mobiles()
    response_data['mobiles_brand_nation_equals_made_in'] = mobiles_brand_nation_equals_made_in()
    return HttpResponse(json.dumps(response_data), content_type="application/json")