from django.shortcuts import render
from django.views.generic import TemplateView

class first_view(TemplateView):
	template_name = 'suvbra/home.html'