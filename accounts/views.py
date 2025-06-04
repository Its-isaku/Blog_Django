
#? Nesesary imports
from django.views.generic import CreateView 
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

#? SignUpView class for user registration
class SignUpView(CreateView):
    template_name = "registration/signup.html"                     #* Template for the signup page
    form_class = UserCreationForm                                  #* Form for user creation
    success_url = reverse_lazy("login")                            #* Redirect URL after successful signup
    