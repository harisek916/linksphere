# import from django
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.views.generic import View
from django.views.generic import FormView,CreateView,TemplateView,UpdateView,DetailView
# import from social app
from social.forms import RegistrationForm,LoginForm,UserProfileForm
from social.models import UserProfile

# Create your views here.

class SignUpView(CreateView):
    template_name="register.html"
    form_class=RegistrationForm

    def get_success_url(self):
        return reverse("signin")

    # def post(self,request,*args,**kwargs):
    #     form=RegistrationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("signup")
    #     else:
    #         return render(request,"register.html",{"form":form})
        
    
class SignInView(FormView):
    template_name="login.html"
    form_class=LoginForm

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user_object=authenticate(request,username=uname,password=pwd)
            if user_object:
                login(request,user_object)
                print("logged in successfully......")
                return redirect("index")
            
        print("error in login")
        return render(request,"login.html",{"form":form})

class IndexView(TemplateView):
    template_name="index.html"

class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")
    


# localhost:8000/profiles/<int:pk>/change/

class ProfileUpdateView(UpdateView):
    template_name="profile_add.html"
    form_class=UserProfileForm
    model=UserProfile

    def get_success_url(self):
        return reverse("index")
    
# localhost:8000/profiles/<int:pk>
    
class ProfileDetailView(DetailView):
    template_name="profile_detail.html"
    model=UserProfile
    context_object_name="data"


