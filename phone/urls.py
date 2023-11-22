from django.urls import path
from .views import BrandList, BrandDetail, PhoneList, PhoneDetail, PhoneSold

# Create your url patterns here
urlpatterns = [
    # Define the url pattern for the brand list view
    path("brands/", BrandList.as_view(), name="brand-list"),
    # Define the url pattern for the brand detail view
    path("brands/<int:pk>/", BrandDetail.as_view(), name="brand-detail"),
    # Define the url pattern for the phone list view
    path("phones/", PhoneList.as_view(), name="phone-list"),
    # Define the url pattern for the phone detail view
    path("phones/<int:pk>/", PhoneDetail.as_view(), name="phone-detail"),
    # Define the url pattern for the phone sold view
    path("phones/<int:pk>/sold/", PhoneSold.as_view(), name="phone-sold"),
]