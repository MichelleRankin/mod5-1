from django.http.response import HttpResponse
from django.shortcuts import render
from app.forms import HelloForm

def root(request):
    context = {}
    if request.method == "GET":
        form = HelloForm(request.GET)
        if form.is_valid():
            context['greeting_success'] = True
        else:
            form = HelloForm()
        context['form'] = form
        return render(request, "root.html", context)

        