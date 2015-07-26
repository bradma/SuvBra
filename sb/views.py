from django.shortcuts import render
from django.views.generic import TemplateView

from sb.models import customer
from sb.forms import customer_form

class first_view(TemplateView):
    template_name = 'suvbra/home.html'
    model = customer

    def post(self, *args, **kwags):
        context = self.get_context_data()
        if context['form'].is_valid():
            print ('Worked')

    def get_context_data(self, **kwargs):
        context = super(first_view, self).get_context_data(**kwargs)
        context['customer_info'] = customer.objects.all()
        form = customer_form(self.request.POST or None)
        context['form'] = form
        return context