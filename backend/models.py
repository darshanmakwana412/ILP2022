from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    title = models.CharField(max_length=500)
    company = models.CharField(max_length=500)
    details = models.TextField()
    place = models.CharField(max_length=500)
    stipend = models.CharField(max_length=500)
    learnings = models.CharField(max_length=5000, null=True)
    branch = models.CharField(max_length=6000, null=True)
    year = models.CharField(max_length=5000, null=True)
    prereq = models.CharField(max_length=400)
    deliverables = models.CharField(max_length=400)
    duration = models.CharField(max_length=500)
    def __str__(self):
        return f"{self.title}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    email = models.CharField(max_length=500, null=True)
    password = models.CharField(max_length=50, blank=True)
    fullname = models.CharField(max_length=100, blank=True)
    rollno = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=100, blank=True)
    yos = models.CharField(max_length=100, blank=True)
    phoneno = models.CharField(max_length=100, blank=True)
    resume = models.FileField(upload_to='resume', blank=True)
    # linkedin = models.CharField(max_length=100, blank=True)
    # experience = models.CharField(max_length=500, blank=True)
    # goal = models.CharField(max_length=500, blank=True)
    # obstacle = models.CharField(max_length=500, blank=True)
    pref_1 = models.IntegerField(blank=True, null=True)
    pref_2 = models.IntegerField(blank=True, null=True)
    pref_3 = models.IntegerField(blank=True, null=True)
    pref_4 = models.IntegerField(blank=True, null=True)
    pref_5 = models.IntegerField(blank=True, null=True)
    submitted = models.BooleanField(default=False)

# Create your models here.
class Phonathon_data(models.Model):
    alum_id = models.CharField(max_length=10, blank=True)
    alum_name = models.CharField(max_length=255, blank=True)
    phone1 = models.CharField(max_length=20, blank=True)
    phone2 = models.CharField(max_length=20, blank=True)
    phone3 = models.CharField(max_length=20, blank=True)
    duration = models.IntegerField(blank=True, null=True)
    stud_name = models.CharField(max_length=255, blank=True)
    ldap = models.CharField(max_length=255, blank=True)