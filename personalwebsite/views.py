from django.views.generic import TemplateView,FormView
from django.shortcuts import render


class HomePage(TemplateView):
    template_name = 'index.html'
