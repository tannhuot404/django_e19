from django.shortcuts import render, redirect
from .models import Category

# Create your views here.
def index(request):
    data = Category.objects.all()
    return render(request, "category/index.html", {"data": data})

def create(request):

    if request.method == 'POST':
        cate_name = request.POST.get('name')

        if cate_name:
            print(f"Category Name: {cate_name}")
            Category.objects.create(
                name = cate_name
            )
            return redirect('category:index')

    return render(request, 'category/create.html')

def edit(request, item_id):

    if request.method == 'POST':
        cate_name = request.POST.get('name')
        cate = Category.objects.get(id=item_id)

        if cate_name and cate:
            print(f"Category Name: {cate_name}")
            cate.name = cate_name
            cate.save()
            return redirect('category:index')
        
    cate = Category.objects.get(id=item_id)

    return render(request, 'category/edit.html', {'data': cate.name})