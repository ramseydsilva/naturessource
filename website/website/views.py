from django.shortcuts import render_to_response

def home(request):
    return render_to_response('home.html')

def nav(request, nav_slug):
    from website.models import Nav
    nav = Nav.objects.get(slug=nav_slug)
    return render_to_response('nav.html', {'nav': nav})
