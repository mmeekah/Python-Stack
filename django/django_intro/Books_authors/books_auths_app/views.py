from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.
def index(request):
    context={
        'all_books': Book.objects.all(),
        'all_authors': Author.objects.all()
    }
    return render(request, 'index.html', context)


def add_book(request):
    print(request.POST)

    new_book =  Book.objects.create(
        title=request.POST['title'],
        desc =request.POST['desc']
    )
    return redirect('/')

def add_author(request):
    print(request.POST)

    
    Author.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        notes=request.POST['notes'],
        
        
    )
    
    return redirect('/')

def display_author_dets(request, auth_id):
    to_exclude = [book.id for book in Author.objects.get(id=auth_id).books.all()]
    context = {
        "author" : Author.objects.get(id=auth_id),
        "author_books" : Author.objects.get(id=auth_id).books.all(),
        "all_books" : Book.objects.exclude(id__in=to_exclude),
    }
    return render(request, "author_view.html", context)

def add_author_to_book(request):
    if request.method == "POST":
        book_id = request.POST["b_id"]
        author_id = request.POST["a_id"]
        Book.objects.get(id=book_id).authors.add(Author.objects.get(id=author_id))
    return redirect("/book_dets/"+book_id)

    
def add_book_to_author(request):
    if request.method == "POST":
        book_id = request.POST["b_id"]
        author_id = request.POST["a_id"]
        Author.objects.get(id=author_id).books.add(Book.objects.get(id=book_id))
    return redirect("/author_dets/"+author_id)   

def display_book_dets(request,book_id):
    to_exclude = [author.id for author in Book.objects.get(id=book_id).authors.all()]
    context = {
        "book" : Book.objects.get(id=book_id),
        "book_authors" : Book.objects.get(id=book_id).authors.all(),
        "all_authors" : Author.objects.exclude(id__in=to_exclude),
    }
    return render(request, "book_view.html", context)
