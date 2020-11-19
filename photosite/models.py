from django.db import models


class Contact(models.Model):
    bride_name = models.CharField(max_length=30)
    groom_name = models.CharField(max_length=30)
    email = models.EmailField(verbose_name="email", max_length=60)
    phone = models.CharField(max_length=10)
    referrals = models.TextField(max_length=200)




