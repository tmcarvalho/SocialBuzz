from django.db import models

# Create your models here.
class FacebookPage(models.Model):
    page_id = models.CharField(blank=False, max_length=100)
    name = models.CharField(blank=True, max_length=100)
    url = models.CharField(blank=True, max_length=100)
    created_at = models.DateTimeField(auto_now=True)

class Person(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=256, primary_key=True)

class Post(models.Model):
    person = models.ForeignKey(Person)
    message = models.TextField(null=True)
    picture = models.URLField(null=True)
    link = models.URLField(null=True)
    name = models.CharField(null=True,max_length=100)
    description = models.TextField(null=True)
    type = models.CharField(max_length=100)
    created_time = models.DateTimeField()
    shares = models.IntegerField(null=True)
    likes = models.IntegerField()
    love = models.IntegerField()
    wow = models.IntegerField()
    haha = models.IntegerField()
    sad = models.IntegerField()
    angry = models.IntegerField()
    id = models.CharField(max_length=256, primary_key=True)