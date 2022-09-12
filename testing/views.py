from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response
# request handeler
# some frameworks called an action


# 1st iteration, function to return HttpResponse using 'return HttpResponse('Hello World')'
# 2nd iteration, renders html response using render fucntion 'return render(request, 'hello.html')'
# 3rd iteration, renders html response in hello.html template using render function 'return render(request, 'hello.html', {'name': 'James'})
# passing a dictionary. From Templates video.


def say_hello(request):
    return render(request, 'hello.html', {'name': 'James'})
    



