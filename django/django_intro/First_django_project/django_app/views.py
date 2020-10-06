from django.shortcuts import render, HttpResponse, redirect


# Create your views here.
def root(request):
    return redirect("/redirected_route")

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    print("Redirected to /")
    return redirect("/")

def show(request, number):
    return HttpResponse("Placeholder to DISPLAY blog {number}")

def edit(request,number):
    return HttpResponse("Placeholder to EDIT blog {number}")

def destroy(request, number):
    return redirect('/')

# def json_file(request):
#     return JsonResponse({"title": "My first blog", "content": "Lorem, ipsum dolor"})

def index2(request):
    context = {
    	"name": "Noelle",
    	"favorite_color": "turquoise",
    	"pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request, "index.html", context)
