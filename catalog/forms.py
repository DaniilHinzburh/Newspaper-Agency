from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from catalog.models import Topic, Redactor, Newspaper


class NewspaperForm(forms.ModelForm):
    topics = forms.ModelMultipleChoiceField(
        queryset=Topic.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Newspaper
        fields = "__all__"
        widgets = {
            'pub_date': forms.DateInput(attrs={'type': 'date'}),
        }


class RedactorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "years_of_experience",
            "first_name",
            "last_name",
            "email"
        )


class RedactorUpdateForm(forms.ModelForm):
    class Meta:
        model = Redactor
        fields = (
            "years_of_experience",
            "first_name",
            "last_name",
        )


class RedactorSearchForm(forms.Form):
    username = forms.CharField(
        label="",
        max_length=255,
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Search by username"}
        )
    )


class NewspaperSearchForm(forms.Form):
    topics = forms.CharField(
        label="",
        max_length=255,
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Search by topic"}
        )
    )


class TopicSearchForm(forms.Form):
    name = forms.CharField(
        label="",
        max_length=255,
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name"}
        )
    )
