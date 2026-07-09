from django.db import models

class QuoteRequest(models.Model):

    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    
    PROJECT_TYPES = [
        ("Basement Renovation", "Basement Renovation"),
        ("Kitchen Renovation", "Kitchen Renovation"),
        ("Bathroom Renovation", "Bathroom Renovation"),
        ("Flooring", "Flooring"),
        ("Painting", "Painting"),
        ("Home Addition", "Home Addition"),
        ("Full Home Renovation", "Full Home Renovation"),
        ("Other", "Other"),
    ]
    BASEMENT_STATUS_CHOICES = [
        ("", "Not Applicable"),
        ("Unfinished Basement", "Unfinished Basement"),
        ("Partially Finished Basement", "Partially Finished Basement"),
        ("Finished Basement Remodel", "Finished Basement Remodel"),
    ]
    BUDGET_CHOICES = [
        ("Under $10,000", "Under $10,000"),
        ("$10,000 - $25,000", "$10,000 - $25,000"),
        ("$25,000 - $50,000", "$25,000 - $50,000"),
        ("$50,000 - $100,000", "$50,000 - $100,000"),
        ("$100,000+", "$100,000+"),
    ]
    TIMELINE_CHOICES = [
        ("ASAP", "ASAP"),
        ("Within 1 Month", "Within 1 Month"),
        ("1-3 Months", "1-3 Months"),
        ("3-6 Months", "3-6 Months"),
        ("Just Planning", "Just Planning"),
    ]
    CONTACT_METHOD_CHOICES = [
        ("Phone", "Phone"),
        ("Email", "Email"),
        ("Text Message", "Text Message"),
    ]
    project_type = models.CharField(
        max_length=100,
        choices=PROJECT_TYPES
    )

    basement_status = models.CharField(
        max_length=100,
        choices=BASEMENT_STATUS_CHOICES,
        blank=True,
        null=True
    )

    budget = models.CharField(
        max_length=50,
        choices=BUDGET_CHOICES,
        blank=True,
        null=True
    )

    timeline = models.CharField(
        max_length=50,
        choices=TIMELINE_CHOICES,
        blank=True,
        null=True
    )

    description = models.TextField()

    contact_method = models.CharField(
        max_length=20,
        choices=CONTACT_METHOD_CHOICES,
        default="Phone"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    
class QuotePhoto(models.Model):
    quote_request = models.ForeignKey(
        QuoteRequest,
        on_delete=models.CASCADE,
        related_name="quote_photos"
    )
    image = models.ImageField(
        upload_to="quote_photos/"
    )

