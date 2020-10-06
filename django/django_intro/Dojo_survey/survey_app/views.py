from django.shortcuts import render

def index(request):

    return render(request, "index.html")

def result(request):
    print(request.POST)
    name = request.POST['name']
    location = request.POST['location']
    language = request.POST['language']
    comment = request.POST['comment']
    context = {
        "name_to_template": name,
        "location_to_template": location,
        "language_to_template": language, 
        "comment_to_template": comment

    }
    return render(request, "result.html",context )
