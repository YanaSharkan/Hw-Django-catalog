from django import forms

from triangle.models import Person


class TriangleForm(forms.Form):
    leg_1 = forms.IntegerField(label='Leg 1', min_value=1)
    leg_2 = forms.IntegerField(label='Leg 2', min_value=1)


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email']
