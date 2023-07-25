from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import *
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .graph import *





def home(request):
    return render(request, 'ghec/home.html')



def clientHome(request):
    client = Client.objects.get(user_id=request.user.id)
    
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('clienthome')
    else:
        form = ClientForm(instance=client)
    
    applications= Application.objects.filter(client_name_id = request.user)
    receipts= Receipt.objects.filter(client_name_id = request.user)
    
    context = {'form': form,  'applications':applications, 'receipts':receipts}
    return render(request, 'ghec/clientHome.html', context)


def adminHome(request):
    data1= client_counts[0]
    data2= client_counts[1]
    data3= client_counts[2]
    data4= client_counts[3]

    name1= countries1[0]
    name2= countries1[1]
    name3= countries1[2]
    name4= countries1[3]

    debtor1= debtor[0]
    debtor2= debtor[1]
    debtor3= debtor[2]
    debtor4= debtor[3]

    amt1= amt[0]
    amt2= amt[1]
    amt3= amt[2]
    amt4= amt[3]

    

    context ={
            'data1':data1,
            'data2':data2,
            'data3':data3,
            'data4':data4,

            'name1':name1,
            'name2':name2,
            'name3':name3,
            'name4':name4,

            'debtor1':debtor1,
            'debtor2':debtor2,
            'debtor3':debtor3,
            'debtor4':debtor4,

            'amt1':amt1,
            'amt2':amt2,
            'amt3':amt3,
            'amt4':amt4,
        }

    return render(request, 'ghec/adminHome.html', context)


def admintest(request):
    data1= client_counts[0]
    data2= client_counts[1]
    data3= client_counts[2]
    data4= client_counts[3]

    name1= countries1[0]
    name2= countries1[1]
    name3= countries1[2]
    name4= countries1[3]
    

    context ={
            'data1':data1,
            'data2':data2,
            'data3':data3,
            'data4':data4,

            'name1':name1,
            'name2':name2,
            'name3':name3,
            'name4':name4,        
        }

    return render(request, 'ghec/admintest.html', context)



def ielts(request):
    document_url = "https://www.docdroid.net/file/download/SJT6EXm/listening-pdf.pdf"
    context = {
        'document_url': document_url,
    }


    return render(request, 'ghec/ielts.html', context)


def aboutUs(request):
    return render(request, 'ghec/about.html')

def packageCanada(request):
    return render(request, 'ghec/packageCanada.html')

def contact(request):
    return render(request, 'ghec/contact.html')

'''
def application(request):
    return render(request, 'ghec/application.html')
'''



def clientlist(request):
    clients= Client.objects.all()
    
    context= {'clients':clients}
    return render(request, 'ghec/clientList.html', context)


def update_client(request, pk): 
    client = Client.objects.get(user_id=pk) 
    form= ClientForm(request.POST or None, instance=client)
    if form.is_valid():
        form.save()
        return redirect('clientlist')
    
    context= {'client':client,'form':form}
    return render(request, 'ghec/updateClient.html', context)

def delete_client(request, pk): 
    client = Client.objects.get(user_id=pk) 
    client.delete()
    return redirect('clientlist')

class application (CreateView):
    model = Application
    form_class = ApplicationForm
    template_name = 'ghec/application.html'
    success_url = reverse_lazy('clienthome')

def applicationlist(request):
    applications= Application.objects.all()
    
    context= {'applications':applications}
    return render(request, 'ghec/applicationList.html', context)


def update_application(request, pk): 
    application = Application.objects.get(id=pk) 
    form= ApplicationForm2(request.POST or None, instance=application)
    if form.is_valid():
        new_debt= form.save(commit=False)
        new_debt.debt= int(new_debt.processing_fee) - int(new_debt.amount_paid)
        new_debt.save()
        messages.success(request, "Successfully Added Product")

        return redirect('applicationlist')
    
    context= {'application':application,'form':form}
    return render(request, 'ghec/updateApplication.html', context)
    

def delete_application(request, pk): 
    application = Application.objects.get(id=pk) 
    application.delete()
    return redirect('applicationlist')


'''
class receipt (CreateView):
    model = Receipt
    form_class = ReceiptForm
    template_name = 'ghec/receipt.html'
    success_url = reverse_lazy('clienthome')

'''

def receipt (request):
    form = ReceiptForm()
    if request.method == 'POST':  # A HTTP POST?
        form = ReceiptForm(request.POST)
        if form.is_valid(): # Have we been provided with a valid form?
            form.save(commit=True) # Save the new information to the database.
            return redirect('clienthome')
        else:
            print(form.errors)

    form = {'form': form}
    return render(request, 'ghec/receipt.html', form)