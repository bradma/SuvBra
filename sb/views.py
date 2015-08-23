from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, DetailView

from sb.serializers import CustSerializer
from sb.models import customer
from sb.forms import customer_form, login_form

class login_view(View):
    template_name = 'login/login.html'
    form_class = login_form

    def get(self, request):
        context = {'form': self.form_class()}
        return render(request, self.template_name, context)

    def post(self, request):
        context = {'form': self.form_class()}
        form = self.form_class(self.request.POST or None)
        if form.is_valid():
            this_user = form['user_name'].data
            this_pass = form['user_pass'].data
            get_user_logged = authenticate(username=this_user, password=this_pass)
            if get_user_logged:
                if get_user_logged.is_active:
                    login(request, get_user_logged)
                    return HttpResponseRedirect(reverse('test:concept_1'))
                else:
                    return HttpResponse('Account Disabled... ')
            else:
                return render(request, self.template_name, context)
        else:
            return render(request, self.template_name, context)

class first_view(View):
    template_name = 'suvbra/home.html'
    form_class = customer_form

    def get(self, request, *args, **kwags):
        context = {
            'form': self.form_class(),
            'customer_info': customer.objects.all(),
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {
            'form': self.form_class(),
            'customer_info': customer.objects.all(),
        }
        form = self.form_class(self.request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, self.template_name, context)

@login_required
def main_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

class customer_detail(DetailView):
    template_name = 'suvbra/cus_detail.html'
    model = customer

class cust_viewset(viewsets.ReadOnlyModelViewSet):
    queryset = customer.objects.all()
    serializer_class = CustSerializer