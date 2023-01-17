from djongo import models

class Respon(models.Model):
    tag = models.CharField(max_length=50)
    patterns = models.CharField(max_length=400)

class Responses(models.Model):
    tag = models.CharField(max_length=50)
    responses = models.CharField(max_length=400)