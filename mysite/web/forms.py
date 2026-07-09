from django import forms
from .models import QuoteRequest

class QuoteRequestForm(forms.ModelForm):
    class Meta:
        model = QuoteRequest
        fields = [
            "full_name",
            "phone",
            "email",
            "address",
            "city",
            "postal_code",
            "project_type",
            "basement_status",
            "budget",
            "timeline",
            "description",
            "contact_method",
        ]