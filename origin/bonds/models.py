from django.db import models
from django.contrib.auth.models import User
import requests

def get_legal_name(lei):   #uses GLEIF api to retrieve LegalName based on LEI
        url = "https://api.gleif.org/api/v1/lei-records/"+str(lei)
        legal_name=requests.get(url).json()['data']['attributes']['entity']['legalName']['name']
        return legal_name

class Bond(models.Model):
    isin = models.CharField(max_length=12)
    size = models.IntegerField()
    currency = models.CharField(max_length=3, default='GBP')
    maturity = models.DateField()
    lei = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    legal_name = models.CharField(max_length=50, default="AUTO FILLS FROM LEI")

    def save(self, *args, **kwargs):    #override default save method to first get legal_name based on LEI current entry
        self.legal_name = get_legal_name(self.lei)
        super(Bond, self).save(*args, **kwargs) 

    def __str__(self):
        return self.legal_name
