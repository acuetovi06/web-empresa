from django.shortcuts import render, get_object_or_404 
from .models import Post, Category # Import the Post and Category models from the models module

# Create your views here.
def blog(request):
    posts = Post.objects.all()  # Retrieve all posts from the database
    return render(request, 'blog/blog.html', {'posts': posts}) # Render the blog template with the posts context

def category(request, category_id):
    # category = Category.objects.get(id=category_id)  # Get the category object by its ID
    category = get_object_or_404(Category, id=category_id)  # Get the category object or return a 404 error if not found
    # posts = Post.objects.filter(categories=category)  # Filter posts by the selected category
    # Una posibilidad de obtenter los posts y retornarlos en la respuestas.
    # Pero una mejor es hacer una búsqueda inversa en el template, donde se buscan
    # todos los posts que tienen la categoría seleccionada.
    return render(request, 'blog/category.html', {'category': category})  # Render the category template with the category context