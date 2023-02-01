from django import forms


class TriangleForm(forms.Form):
    leg_1 = forms.IntegerField(label='Leg 1', min_value=1)
    leg_2 = forms.IntegerField(label='Leg 2', min_value=1)
