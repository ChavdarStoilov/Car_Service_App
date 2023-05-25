from django.views.generic import TemplateView
from django.shortcuts import render

class IndexView(TemplateView):
    template_name ='customer/index.html'
