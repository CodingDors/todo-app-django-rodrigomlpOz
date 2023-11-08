from django.shortcuts import render

tasks = []

# Create your views here.
def index(request):
    # TODO
    return render(request, "tasks/index.html")
