#Reports     
from .models import Brand, Mobile
from django.db.models import F

def all_brands_in_korea():
    query = Brand.objects.filter(nationality='Korea')
    return query

def some_brand_mobiles(*brand_names):
    query = Mobile.objects.filter(brand__name__in=brand_names)
    return query

def mobiles_brand_nation_equals_made_in():
    query = Mobile.objects.filter(brand__nationality=F('made_in'))
    return query