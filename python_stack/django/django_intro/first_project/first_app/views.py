from django.shortcuts import render,httpResponse,redirect
from django.http import JsonResponse

# Create your views here.
def root(request):
    return redirect("/blogs")

def index(request):
    return httpResponse("placeholder to later display a list of all blogs")
    
def new(request):
    return httpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/")

def show(request, number):
    return httpResponse("placeholder to display blog number: {number}")
    
def edit(request, number):
    return httpResponse("placeholder to edit blog {number}")
    
def destroy(request, number):
    return redirect("/blogs")

def blogs_json(request):
    data = {
        "title": "My First Blog",
        "content": "This is the content of the blog."
    }

    return JsonResponse(data)
