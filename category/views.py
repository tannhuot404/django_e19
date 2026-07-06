from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, "category/index.html")

def create(request):

    if request.method == 'POST':
        name = request.POST.get('name')

        if name:
            print(f"Category Name: {name}")
            return redirect('category:index')

    return render(request, 'category/create.html')