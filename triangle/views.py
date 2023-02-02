from math import sqrt
from django.shortcuts import render

from .forms import TriangleForm


def calculate_triangle(request):
    form = TriangleForm(request.GET)
    params = {"form": form}
    if form.is_valid():
        form.clean()
        leg_1 = form.cleaned_data.get("leg_1")
        leg_2 = form.cleaned_data.get("leg_2")
        params["result"] = round(sqrt(leg_1**2 + leg_2**2), 2)
    return render(request, "triangle/triangle.html", params)
