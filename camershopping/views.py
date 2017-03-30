from django.shortcuts import render



def page404 (request):
    template = "404.html"
    render (request, template)


def page500 (request):
    template = "500.html"
    render (request, template)