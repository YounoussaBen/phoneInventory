from django.db import models
from django.utils import timezone

# Create your model for brand here
class Brand(models.Model):
    # Define the field for the brand name
    name = models.CharField(max_length=100, unique=True)

    # Define a method to return a string representation of the brand
    def __str__(self):
        return self.name

# Create your model for phone here
class Phone(models.Model):
    # Define the fields for name, price, sold and date
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sold = models.BooleanField(default=False)
    date = models.DateField(null=True, blank=True)

    # Define a foreign key field to link the phone name to the brand
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="phones")

    # Define a method to mark the phone as sold and set the date
    def mark_as_sold(self):
        self.sold = True
        self.date = timezone.now().date()
        self.save()

    # Define a method to return a string representation of the phone
    def __str__(self):
        return f"{self.name} by {self.brand} for {self.price}"
