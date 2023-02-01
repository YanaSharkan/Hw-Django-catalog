from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import TriangleForm


def calculate_triangle(request):
    params = {}
    if request.GET.get('hypotenuse'):
        params['result'] = round(float(request.GET.get('hypotenuse')), 3)
    elif request.method == 'POST':
        form = TriangleForm(request.POST)
        if not form.is_valid():
            params['error'] = 'Triangle\'s legs should be > 0'
        else:
            form.clean()
            leg_1 = form.cleaned_data.get("leg_1")
            leg_2 = form.cleaned_data.get("leg_2")
            hypotenuse = (leg_1**2 + leg_2**2)**0.5
            return redirect(reverse("triangle:triangle") + "?hypotenuse=" + str(hypotenuse))
    return render(request, 'triangle/triangle.html', params)
