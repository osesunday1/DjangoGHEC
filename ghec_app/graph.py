from .models import *
from django.shortcuts import render
from django.db.models import Count

'''
name= []
data= []
queryset  = Application.objects.order_by('-phone')[:6]

for person in queryset:
    name.append(person.country)
    data.append(person.phone)
        
    


def client_count_by_country(request):
    # Query the database to count clients per country
    country_counts = Application.objects.values('country').annotate(client_count=Count('client_name'))[:6]

    # Create an array to store the country counts
    country_count_array = []
    for country in country_counts:
        country_count_array.append({
            'country': country['country'],
            'client_count': country['client_count']
        })

    # Return the country count array as a JSON response
    return JsonResponse(country_count_array, safe=False)

    



   
name= []
data= []
queryset  = Application.objects.order_by('-amount_paid')[:6]

for person in queryset:
    name.append(person.client_name)
    data.append(person.amount_paid)

'''


countries1 = []
client_counts = []

country_counts = Application.objects.values('country').annotate(client_count=Count('client_name')).order_by('-client_count')[:4]

for country in country_counts:
    countries1.append(country['country'])
    client_counts.append(country['client_count'])



debtor= []
amt= []
queryset  = Application.objects.order_by('-debt')[:4]

for person in queryset:
    debtor.append(person.client_name.first_name)
    amt.append(person.debt)