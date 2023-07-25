from django.contrib import admin
from ghec_app.models import User 
from .models import *




@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display= ('email',)
    ordering=('email',)
    search_fields= ('email',)
#admin.site.register(User)

@admin.register(Client)
class UserAdmin(admin.ModelAdmin):
    fields= (('first_name', 'last_name'), 'address', 'phone',)
    list_display= ('first_name','last_name', 'address', 'phone',)
    list_filter = ('first_name','last_name', 'address', 'phone',)
    ordering=('first_name',)
    search_fields= ('first_name',)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'package', 'processing_fee', 'amount_paid', 'debt','date_created','ielts',) 
    ordering= ('package',)
    search_fields= ('package', 'client_name')


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'amount_paid', 'sender_name', 'date_paid', 'bank_name','reason',) 
    ordering= ('date_paid',)
    search_fields= ('date_paid', 'client_name')