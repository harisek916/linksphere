# import from django
from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic import View
from django.views.generic import FormView,CreateView
# import from social app
from social.forms import RegistrationForm

# Create your views here.

class SignUpView(CreateView):
    template_name="register.html"
    form_class=RegistrationForm

    def get_success_url(self):
        return reverse("signup")

    # def post(self,request,*args,**kwargs):
    #     form=RegistrationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("signup")
    #     else:
    #         return render(request,"register.html",{"form":form})
        
    
