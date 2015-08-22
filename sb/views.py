from django.shortcuts import render
from rest_framework import viewsets
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
        print ('Pass for Now')

"""
class main_login(View):
    template_name = 'login.html'
    form_class = my_login

    def get(self, request, *args, **kwargs):
        context = {'form': self.form_class()}
        return render(request, self.template_name, context)

    def post (self, request, *args, **kwargs):
        context = {'form': self.form_class()}
        form = self.form_class(self.request.POST or None)
        if form.is_valid():
            _username = request.POST['username']
            _password = request.POST['password']
            userlogin = authenticate(username=_username, password=_password)
            if userlogin:
                if userlogin.is_active:
                    login(request, userlogin)
                    return HttpResponseRedirect(reverse('main'))
                else:
                    return HttpResponse('Invalid')
            else:
                return HttpResponse('Invalid Username or Password')
        return render(request, self.template_name, context)
"""



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

class customer_detail(DetailView):
    template_name = 'suvbra/cus_detail.html'
    model = customer

class cust_viewset(viewsets.ReadOnlyModelViewSet):
    queryset = customer.objects.all()
    serializer_class = CustSerializer