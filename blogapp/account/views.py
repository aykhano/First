from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def login_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "account/login.html", {
                "error": "Invalid name or parol"
            })

    return render(request, "account/login.html")

def register_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request, "account/register.html", 
                {
                    "error":"username is exist", 
                    "username":username,
                    "email":email,
                    "firstname":firstname,
                    "lastname":lastname,
                    "username":username,
                })
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, "account/register.html", 
                    {
                        "error":"email is exist", 
                        "username":username,
                        "email":email,
                        "firstname":firstname,
                        "lastname":lastname,
                        "username":username,
                    })
                else:
                    user = User.objects.create_user(username=username, email=email, first_name=firstname, 
                    last_name=lastname, password=password)
                    user.save()
                    return redirect("login")
        else:
            return render(request, "account/register.html", 
            {
                "error":"password is wrong!",
                "error":"email is exist", 
                "username":username,
                "email":email,
                "firstname":firstname,
                "lastname":lastname,
                "username":username,

            })

    return render(request, "account/register.html")

def logout_request(request):
    return redirect("home")
