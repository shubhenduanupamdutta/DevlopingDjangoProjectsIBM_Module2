# Create your views here.
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    # Create a simple html page as a string
    template = "<html>This is your first view</html>"
    # Return the template as content argument in HTTP response
    return HttpResponse(content=template)
