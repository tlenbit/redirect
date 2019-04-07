from django.db import models


class Webmaster(models.Model):
    name = models.CharField(max_length=255)
    url =  models.CharField(max_length=2083)

class Offer(models.Model):
    name = models.CharField(max_length=255)
    url =  models.CharField(max_length=2083)

class Click(models.Model):
    webmaster = models.ForeignKey('Webmaster', on_delete=models.CASCADE)
    offer = models.ForeignKey('Offer', on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)

    client_user_agent = models.CharField(max_length=255)
    client_ip = models.CharField(max_length=255)
    client_country = models.CharField(max_length=255)
    client_timezone = models.CharField(max_length=255)
    client_city = models.CharField(max_length=255)
