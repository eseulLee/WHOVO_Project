from django.db import models
from userApp.models import WebMember

# Create your models here.
'''
class WebMember(models.Model):
    member_id = models.TextField(max_length=100, primary_key=True)
    member_pwd = models.TextField(max_length=100)
    member_name = models.TextField(max_length=100, unique=True)
    member_poli = models.TextField(max_length=100)
    member_age = models.IntegerField()
    member_regdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.member_id+"\t"+self.member_pwd+"\t"+self.member_name
'''
class Post(models.Model):
    # id(pk), writer_id, writer_name, content, regdate, viewcnt
    id            = models.BigAutoField(help_text = "Post ID", primary_key=True)
    candidate_num = models.IntegerField
    detail_num    = models.IntegerField
    writer_id     = models.ForeignKey("userApp.WebMember", on_delete=models.CASCADE, db_column='writer_id', help_text= "post writer ID")
    content       = models.TextField(blank=False, null=False)
    create_date   = models.DateTimeField(auto_now=True)
    modify_date   = models.DateTimeField(auto_now=True)
'''
    def __str__(self):
        return self.id+"\t"+self.writer_id
'''
class Comment(models.Model):
    # id(pk), contents, writer_id, writer_name, bbs_id(fk)
    post         = models.ForeignKey("Post", on_delete=models.CASCADE, db_column="post")
    id           = models.BigAutoField(help_text = "comment ID", primary_key=True)
    writer_id    = models.ForeignKey("userApp.WebMember", on_delete=models.CASCADE, db_column="writer_id", related_name= 'comment', help_text= "comment writer ID")
    contents     = models.TextField(blank=False, null=False)
    create_date  = models.DateTimeField(auto_now=True)
    modify_date  = models.DateTimeField(auto_now=True)
'''
    def __str__(self):
        return self.id+"\t"+self.writer_id
'''
# post, comment 둘다 좋아요 수 미기재