from django import views
from django.shortcuts import render

class IndexView(views.View):
    template_name ='web/index.html'
