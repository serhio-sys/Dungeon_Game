from django.shortcuts import render,redirect
from django.views.generic import TemplateView,UpdateView,ListView
from django.urls import reverse_lazy
from User.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

class MixinRegOrLog():
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formlog"] = LoginUser()
        context['formreg'] = CreateUser()
        return context

class HomePage(TemplateView):
    template_name='home/home.html'
    extra_context={'name':'Home'}

class Registr(MixinRegOrLog,TemplateView):
    template_name='home/logreg.html'
    extra_context={'name':'Login'}

class UpdatePhoto(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Newuser
    fields=['img',]
    template_name='home/upd.html'
    extra_context={'name':'Update Photo'}

    def test_func(self):
        user = Newuser.objects.get(pk=self.kwargs['pk'])
        return self.request.user==user
    
class AllUsers(ListView):
    paginate_by=4
    model=Newuser
    queryset=Newuser.objects.all().order_by('balance')
    template_name='home/top.html'
    extra_context={'name':'Forbes Boycovskiy Club'}
