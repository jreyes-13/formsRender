from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader

from .models import Login
from .forms import LoginForm

# Create your views here.
def index(request):
    form = LoginForm();
    # context = {"form": form}
    context = {}
    template = loader.get_template("index.html");
    return HttpResponse(template.render(context, request));


# def login(request):
#     email = request.POST["email"];
#     pwd = request.POST["password"];

#     # We want to save data to the DB

#     # validate the form
#     if not email or "@" not in email:
#         print("Invalid email")

#     # if form is valid, 
#         # then save data to DB 
#     Login.objects.create(email=email, password=pwd)

#     context = {}
#     template = loader.get_template("index.html");
#     return HttpResponse(template.render(context, request));



def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        # We want to save data to the DB

        # validate the form
        # if form is valid, 
        if form.is_valid():
            # then save data to DB 
            form.save();
            print("Login info saved.");
        else:
            print("Invalid form.");

        # Login.objects.create(email=email, password=pwd)

        context = {}
        template = loader.get_template("index.html");
        return HttpResponse(template.render(context, request));



def details(request):
    detailsList = Login.objects.all 
    context = {"details": detailsList}
    template = loader.get_template("details.html");
    return HttpResponse(template.render(context, request));