from django.db import models


class UserProfile(models.Model):
    serial_number = models.IntegerField()
    resume = models.CharField(max_length=100,null=True,blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    mobile = models.IntegerField(null=True,blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
    work_exp = models.CharField(max_length=100,null=True,blank=True)
    current_loc = models.CharField(max_length=100,null=True,blank=True)
    corrected_loc = models.CharField(max_length=100,null=True,blank=True)
    nearest_city = models.CharField(max_length=100,null=True,blank=True)
    preferred_loc = models.CharField(max_length=100,null=True,blank=True)
    ctc = models.FloatField(max_length=100,null=True,blank=True)
    current_employer = models.CharField(max_length=100,null=True,blank=True)
    current_designation = models.CharField(max_length=100,null=True,blank=True)
    skills = models.CharField(max_length=255,null=True,blank=True)
    ug_course = models.CharField(max_length=255,null=True,blank=True)
    ug_institute = models.CharField(max_length=255,null=True,blank=True)
    ug_passing_yr = models.IntegerField(null=True,blank=True)
