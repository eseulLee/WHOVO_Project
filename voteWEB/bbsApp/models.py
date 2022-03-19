from django.db import models

# Create your models here.

class Post(models.Model):
    # id(pk), writer_id, writer_name, content, regdate, viewcnt
    id            = models.BigAutoField(help_text = "Post ID", primary_key=True)
    candidate_num = models.IntegerField()
    detail_num    = models.IntegerField()
    writer_id     = models.TextField(max_length=100)
    content       = models.TextField(blank=False, null=False)
    create_date   = models.DateTimeField(auto_now=True)
    modify_date   = models.DateTimeField(auto_now=True)
