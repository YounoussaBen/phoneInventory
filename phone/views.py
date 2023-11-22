from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import BrandSerializer, PhoneSerializer
from .models import Brand, Phone

# Create your generic view for brand list here
class BrandList(generics.ListCreateAPIView):
    # Define the serializer class and the queryset
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()

# Create your generic view for brand detail here
class BrandDetail(generics.RetrieveUpdateDestroyAPIView):
    # Define the serializer class and the queryset
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()

# Create your generic view for phone list here
class PhoneList(generics.ListCreateAPIView):
    # Define the serializer class and the queryset
    serializer_class = PhoneSerializer
    queryset = Phone.objects.all()

# Create your generic view for phone detail here
class PhoneDetail(generics.RetrieveUpdateDestroyAPIView):
    # Define the serializer class and the queryset
    serializer_class = PhoneSerializer
    queryset = Phone.objects.all()

# Create your custom view for marking the phone as sold here
class PhoneSold(generics.GenericAPIView):
    # Define the serializer class and the queryset
    serializer_class = PhoneSerializer
    queryset = Phone.objects.all()

    # Define the post method to mark the phone as sold and set the date
    def post(self, request, *args, **kwargs):
        # Get the phone instance from the url parameters
        phone = self.get_object()
        # Call the mark_as_sold method on the phone instance
        phone.mark_as_sold()
        # Return a success response with the updated phone data
        return Response(self.get_serializer(phone).data, status=status.HTTP_200_OK)
