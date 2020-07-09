from django.shortcuts import render, redirect, reverse
from django.contrib.auth import views as auth_views
from .froms import CustomUserCreationForm, customAuthForm


def register(request):
    if(request.user.is_authenticated):
        return redirect('/')
    if(request.method == "POST"):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = CustomUserCreationForm()
        return render(request, "account/signup.html", {"form": form})


class Login(auth_views.LoginView):
    form_class = customAuthForm
    redirect_authenticated_user = True
    template_name = 'account/login.html'
