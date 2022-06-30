from django.shortcuts import redirect
from django.views.generic import View,DetailView,TemplateView,DeleteView
from django.http import JsonResponse
from User.forms import CreateUser
from django.contrib.auth import logout,authenticate,login
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class CreateU(View):
    form_class = CreateUser
     
    def post(self, request,*args, **kwargs):
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'success':True},status=200)
        else:
            return JsonResponse({'error':form.errors},status=203)

class Auth(View):
    def post(self, request,*args, **kwargs):
        user = authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            login(request,user)
            return JsonResponse({'success':True},status=200)
        else:
            return JsonResponse({"error":'This account don`t created or invalid username or password'},status=203)

def Logout(req):
    logout(req)
    return redirect('home')


class User(LoginRequiredMixin,TemplateView):
    template_name='home/user.html'
    extra_context={'name':'Profile'}

class UserDetail(DetailView):
    model=Newuser
    template_name='home/detailuser.html'
    extra_context={'name':'Detail Profile'}
    context_object_name='usr'

class DeleteUSer(LoginRequiredMixin,DeleteView):
    model=Newuser
    success_url ='home'
    extra_context={'name':'Delete Profile'}