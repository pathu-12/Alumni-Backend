from sre_constants import BRANCH
from django.db import models

DEPARTMENTS = (
    ("COMPS","COMPUTER ENGINEERING"),
    ("IT", "INFORMATION TECHNOLOGY ENGINEERING"),
    ("EXTC", "ELECTRONICS AND TELECOMMUNICATION ENGINEERING"),
    ("ETRX","ELECTRONICS ENGINEERING"),
    ("AIDS", "ARTIFICIAL INTELLIGENCE AND DATA SCIENCE ENGINEERING")
)

class Alumni(models.Model):
    name = models.CharField(max_length=50)
    registration_no = models.IntegerField(unique=True)
    passing_year = models.IntegerField()
    branch = models.CharField(choices=DEPARTMENTS, max_length=5)
    email_id = models.EmailField(unique=True)
    company = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image_url = models.URLField(max_length=500, default="")

    def __str__(self):
        return self.name 

class Event(models.Model):
    name = models.CharField(max_length=500)
    schedule = models.DateTimeField()
    description = models.TextField()
    event_image = models.URLField(max_length=500)

    def __str__(self):
        return self.name


class Hiring(models.Model):
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.company