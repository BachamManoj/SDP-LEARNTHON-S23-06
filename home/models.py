from django.db import models


class Voter(models.Model):
    objects = None
    picture = models.ImageField(upload_to='voter_application_pictures/')
    aadhar_number = models.CharField(max_length=12, null=True, blank=True)
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    address = models.TextField()
    pincode = models.CharField(max_length=10)
    mobile_number = models.CharField(max_length=15)
    state = models.CharField(max_length=100)
    parliamentary_constituency = models.CharField(max_length=100)
    assembly_constituency = models.CharField(max_length=100)
