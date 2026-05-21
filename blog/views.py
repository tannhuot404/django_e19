from django.shortcuts import render, redirect
from django.http import HttpResponse

def welcome_view(request):
    return HttpResponse("<h1>Welcom to Django App</h1>")

def search(request):
    search_text = request.GET.get('q', '')

    if search_text:
        return HttpResponse(f"You search for {search_text}")
    
    return HttpResponse("You didn't search anything.")

def post_detail(request, id):
    return HttpResponse(f"Post with id {id}")

def payment(request):
    return redirect('welcome')