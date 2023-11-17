from django.db import models

class Details(models.Model):
    
    title=models.CharField(max_length=200)
    desc=models.CharField(max_length=1000)
    files=models.FileField(upload_to="files/",max_length=250,null=True,default=None)


class Track(models.Model):
    trackid=models.CharField(max_length=100)