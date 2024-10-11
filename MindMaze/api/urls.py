from django.contrib import admin
from django.urls import path
# from api.views import index
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.index, name='index'),
    path('pdfdocuments/', views.pdf_document_list, name='pdf_document_list'),    
    path('pdfdocuments/create/', views.pdf_document_create, name='pdf_document_create')
]

