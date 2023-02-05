from math import sqrt

from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import PersonForm, TriangleForm
from .models import Person


def calculate_triangle(request):
    form = TriangleForm(request.GET)
    params = {"form": form}
    if form.is_valid():
        form.clean()
        leg_1 = form.cleaned_data.get("leg_1")
        leg_2 = form.cleaned_data.get("leg_2")
        params["result"] = round(sqrt(leg_1**2 + leg_2**2), 2)
    return render(request, "triangle/triangle.html", params)


def create_person(request):
    params = {}
    if request.method == "POST":
        form = PersonForm(request.POST)
        params["form"] = form
        if form.is_valid():
            person = form.save()
            return redirect(reverse("person:edit_person", args=(person.id,)))
        else:
            params["error"] = "Invalid person"
            return render(request, "person/person.html", params)
    else:
        params["form"] = PersonForm()
        return render(request, "person/person.html", params)


def edit_person(request, pk):
    obj = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
        form = PersonForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect(reverse("person:edit_person", args=(pk, )))
        else:
            return render(request, "person/edit_person.html", {"form": form, "pk": pk, "error": "Not Updated"})
    else:
        form = PersonForm(instance=obj)
    return render(request, "person/edit_person.html", {"form": form, "pk": pk})
