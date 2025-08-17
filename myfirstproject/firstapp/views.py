# Create your views here.
from datetime import date

from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    # Create a simple html page as a string
    template = "<html>This is your first view</html>"
    # Return the template as content argument in HTTP response
    return HttpResponse(content=template)


def get_date(request: HttpRequest) -> HttpResponse:
    today = date.today()
    template = f"<html>Today's date is {today}</html>"
    return HttpResponse(content=template)
