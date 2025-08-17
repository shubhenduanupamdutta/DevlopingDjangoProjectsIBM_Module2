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


def enroll(request: HttpRequest, course_id: int) -> HttpResponse:
    # If request method is POST
    if request.method == "POST":
        # First try to read the course object
        # If could be found, raise a 404 exception
        course = get_object_or_404(Course, pk=course_id)
        # Increase the enrollment by 1
        course.total_enrollment += 1
        course.save()
        # Return a HTTP response redirecting user to course list view
        return HttpResponseRedirect(
            reverse(viewname="onlinecourse:course_details", args=(course.id,)),  # pyright: ignore[reportAttributeAccessIssue]
        )
    return HttpResponse("Method not allowed", status=405)


def course_details(request: HttpRequest, course_id: int) -> HttpResponse:
    context = {}
    if request.method == "GET":
        try:
            course = Course.objects.get(pk=course_id)
            context["course"] = course
            # Use render() method to generate HTML page by combining
            # template and context
            return render(request, "onlinecourse/course_detail.html", context)
        except Course.DoesNotExist as e:
            # If course does not exist, throw a Http404 error
            msg = "No course matches the given id."
            raise Http404(msg) from e
    return HttpResponse("Method not allowed", status=405)
