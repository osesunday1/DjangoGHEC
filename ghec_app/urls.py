from django.urls import path
from . import views
from .views import *







urlpatterns = [
    path('', views.home, name="home"),
    path ('clienthome', views.clientHome, name= 'clienthome'),
    path ('adminhome', views.adminHome, name= 'adminhome'),
    path ('admintest', views.admintest, name= 'admintest'),


    path('packageCanada', views.packageCanada, name="packageCanada"),
    path('aboutUs', views.aboutUs, name="aboutUs"),
    path('contact', views.contact, name="contact"),
    path('ielts', views.ielts, name="ielts"),
    #path('application', views.application, name="application"),
    path ('application', application.as_view(), name= 'application'),
    path ('clientlist', views.clientlist, name= 'clientlist'),
    path('updateclient/<int:pk>', views.update_client, name="updateclient"),
    path('deleteclient/<int:pk>', views.delete_client, name="deleteclient"),

    path ('applicationlist', views.applicationlist, name= 'applicationlist'),
    path('updateapplication/<int:pk>', views.update_application, name="updateapplication"),
    path('deleteapplication/<int:pk>', views.delete_application, name="deleteapplication"),

    #path ('receipt', receipt.as_view(), name= 'receipt'),
    path('receipt', views.receipt, name= 'receipt'),
]


