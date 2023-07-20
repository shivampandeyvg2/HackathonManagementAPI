from django.db import models
from django.utils import timezone

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
    hackathon_start_date_txt = models.DateTimeField(null=True)
    hackathon_end_date_txt = models.DateTimeField(null=True)
    hackathon_reward_prize = models.CharField(max_length=15)


class HackathonRegistrationsModel(models.Model):
    hackathon_id = models.IntegerField(null=False, blank=False)
    registered_usr_id = models.IntegerField(null=False, blank=False)
    registration_date = models.DateTimeField(default=timezone.now())
