from rest_framework import serializers
from .models import Brand, Phone

# Create your serializer for brand here
class BrandSerializer(serializers.ModelSerializer):
    # Define the meta class to specify the model and the fields
    class Meta:
        model = Brand
        fields = ["name"]

# Create your serializer for phone here
class PhoneSerializer(serializers.ModelSerializer):
    # Define the meta class to specify the model and the fields
    brand = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all())

    class Meta:
        model = Phone
        fields = ["name", "price", "sold", "date", "brand"]

    # Define a read-only field to display the brand name instead of the id
    brand = serializers.StringRelatedField()