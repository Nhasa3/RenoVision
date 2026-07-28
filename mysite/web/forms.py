import re
from django import forms
from django.core.exceptions import ValidationError
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
        
    def clean_full_name(self):
        name = self.cleaned_data.get("full_name", "").strip()
        if len(name) < 2:
            raise ValidationError("Please enter your full name.")
        if not re.match(r"^[A-Za-z\s'\-\.]+$", name):
            raise ValidationError("Name contains invlide characters.")
        return name
    
    def clean_phone(self):
        phone = self.cleaned_data.get("phone", "").strip()
        
    # Reject if it contains anything other than digits, spaces, and standard phone punctuation
        if not re.match(r"^[\d\s\-\(\)\+\.]+$", phone):
            raise ValidationError(
                "Phone number can only contain digits and standard formatting (e.g. dashes, parentheses)."
            )
        digits = re.sub(r"\D", "", phone)
        if len(digits) < 10 or len(digits) > 11:
            raise ValidationError("Enter a valid phone number, e.g. (555) 123-4567.")
        return phone
    
    def clean_postal_code(self):
        postal = self.cleaned_data.get("postal_code", "")
        pattern = r"^[A-Z]\d[A-Z]\s?\d[A-Z]\d$"
        if not re.match(pattern, postal):
            raise ValidationError("Enter a valid postal code, e.g. K1A 0A6.")
        postal = postal.replace(" ", "")
        postal = f"{postal[:3]} {postal[3:]}"
        return postal