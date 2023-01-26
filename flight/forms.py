from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator, MaxLengthValidator

from flight.models import CrewMember


def validate_license():
    license_number = forms.CharField(
        validators=[
            RegexValidator(
                r"[0-9]{5}:[a-zA-Z]{3}",
                "Please ensure the license number format is 00000:XXX,"
                "where 0 is a digit and X is a letter"
            ),
            MaxLengthValidator(9, "License number should be 9 characters max")
        ]
    )
    return license_number


class CrewMemberCreationForm(UserCreationForm):
    license_number = validate_license()

    class Meta(UserCreationForm.Meta):
        model = CrewMember
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "license_number",
        )


class CrewMemberUpdateForm(forms.ModelForm):
    license_number = validate_license()

    class Meta:
        model = CrewMember
        fields = ("license_number", "position")
