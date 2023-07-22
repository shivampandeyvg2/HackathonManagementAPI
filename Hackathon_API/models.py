from django.db import models
from django.utils import timezone
from rest_framework import validators
from rest_framework.exceptions import ValidationError

submission_modes = (
    ('image', 'Image'),
    ('file', 'File'),
    ('link', 'Link')
)


class Hackathon(models.Model):
    hackathon_title_txt = models.CharField(max_length=100)
    hackathon_description_txt = models.TextField(max_length=2000, blank=True)
    hackathon_background_img_path = models.ImageField(upload_to="backgroundImg/", null=True, blank=True)
    hackathon_img_path = models.ImageField(upload_to="Img/", null=True, blank=True)
    hackathon_submission_mode = models.CharField(max_length=10, blank=False, choices=submission_modes)
    hackathon_start_date_txt = models.DateTimeField()
    hackathon_end_date_txt = models.DateTimeField()
    hackathon_reward_prize = models.CharField(max_length=15)
    created_by_usr_id = models.IntegerField( null= False , blank= False)


class HackathonRegistrationsModel(models.Model):
    hackathon_id = models.IntegerField(null=False, blank=False)
    registered_usr_id = models.IntegerField(null=False, blank=False)
    registration_date = models.DateTimeField(default=timezone.now())





class HackathonSubmissions(models.Model):
    submission_name = models.CharField(null= False , blank= False , max_length= 250)
    submission_summary = models.TextField (max_length= 1000)
    submission_type = models.CharField (null= False , blank= False , choices= submission_modes , max_length= 100)
    submission =  models.URLField (null =False , blank= False )
    submitted_by_usr_id = models.IntegerField(null= False)
    hackathon_id = models.IntegerField (null = False)
