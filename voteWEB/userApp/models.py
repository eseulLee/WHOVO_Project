from django.db import models

# Create your models here.

class WebMember(models.Model):
    member_id = models.TextField(max_length=100, primary_key=True)
    member_pwd = models.TextField(max_length=100, blank=False, null=False)
    member_name = models.TextField(max_length=100, blank=False, null=False)
    member_poli = models.TextField(max_length=100, blank=False, null=False)
    member_age = models.DateField()
    member_regdate = models.DateTimeField(auto_now=True)
