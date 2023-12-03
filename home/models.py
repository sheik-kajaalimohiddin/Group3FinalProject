from django.db import models
from django.utils import timezone


class PropertyType(models.Model):
    id = models.AutoField(primary_key=True)
    property_type_name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.property_type_name)


class PropertyNeighborhood(models.Model):
    id = models.AutoField(primary_key=True)
    property_neighborhood_name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.property_neighborhood_name)


class PropertyPricerange(models.Model):
    id = models.AutoField(primary_key=True)
    property_price_range_name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.property_price_range_name)


class Property(models.Model):
    STATUS_CHOICES = (
        ('available', 'AVAILABLE'),
        ('pending', 'PENDING'),
        ('sold', 'SOLD'),
    )

    PROPERTY_CHOICES = (
        (True, 'Yes'),
        (False, 'No')
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='none')
    description = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=3, decimal_places=1)
    square_feet = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    featured_property = models.BooleanField(choices=PROPERTY_CHOICES, default='False')
    flag = models.BooleanField(default=True)
    property_image_main = models.ImageField(upload_to='media/property_images/%Y/%m/%d/', blank=False)
    property_image_1 = models.ImageField(upload_to='media/property_images/%Y/%m/%d/', blank=True)
    property_image_2 = models.ImageField(upload_to='media/property_images/%Y/%m/%d/', blank=True)
    property_image_3 = models.ImageField(upload_to='media/property_images/%Y/%m/%d/', blank=True)
    property_type = models.ForeignKey(PropertyType, on_delete=models.SET_NULL, null=True)
    property_neighborhood = models.ForeignKey(PropertyNeighborhood, on_delete=models.SET_NULL, null=True)
    property_type_price_range = models.ForeignKey(PropertyPricerange, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.name)


class PropertyImage(models.Model):
    id = models.AutoField(primary_key=True)
    property_listing_image_main = models.ImageField(upload_to='media/property_images/%Y/%m/%d/', blank=True)
    property_listing_image_All = models.ImageField(upload_to='media/property_images/%Y/%m/%d/', blank=True)
    property_id = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.property_id)


class Profile(models.Model):
    profile_image = models.ImageField(upload_to='media/property_images/%Y/%m/%d/', blank=True)
    name = models.CharField(max_length=50)
    phonenumber = models.IntegerField(max_length=10)
    email = models.EmailField(max_length=50)
    address = models.TextField(max_length=50)


class Search(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(default=timezone.now)
    property_type = models.ForeignKey(PropertyType, on_delete=models.SET_NULL, null=True)
    property_neighborhood = models.ForeignKey(PropertyNeighborhood, on_delete=models.SET_NULL, null=True)
    property_type_price_range = models.ForeignKey(PropertyPricerange, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.id)


class Event(models.Model):
    picture = models.ImageField(upload_to='media/property_images/%Y/%m/%d/', blank=True)
    description = models.TextField(max_length=500)
