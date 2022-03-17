from django.db import models
import datetime as dt

# Create your models here.

class WebMember(models.Model):
    member_id = models.TextField(max_length=100, primary_key=True)
    member_pwd = models.TextField(max_length=100, blank=False, null=False)
    member_name = models.TextField(max_length=100, blank=False, null=False)
    member_poli = models.TextField(max_length=100, blank=False, null=False)
    member_age = models.DateField()
    member_regdate = models.DateTimeField(auto_now=True)

    # def ageCalc(self, member_age):
    #     birth_year = member_age.dt.date.year
    #     today = dt.date.today().year
    #     age_calc = today - birth_year + 1
    #     return age_calc

