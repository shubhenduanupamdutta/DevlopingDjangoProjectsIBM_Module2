from django.http import Http404, HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import generic

from .models import Course, Enrollment, Lesson


# Create your views here.
def popular_course_list(request: HttpRequest) -> HttpResponse:
    context = {}
    # If the request method is GET
    if request.method == "GET":
        # Using the objects model manage to read all course list
        # and sort them by total_enrollment descending
        course_list = Course.objects.order_by("-total_enrollment")[:10]
        # Appen the course list as an entry of context dict
        context["course_list"] = course_list
        return render(request, "onlinecourse/course_list.html", context)
    return HttpResponse("Method not allowed", status=405)
