from django.shortcuts import render,HttpResponse

# Create your views here.
def blogs(request):
    # return HttpResponse("Hello World ")

    return render(request, 'blogs.html')