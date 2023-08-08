from django.shortcuts import render

# Create your views here.
def webpack(request):
    return render(request, "myapp/hello_webpack.html")