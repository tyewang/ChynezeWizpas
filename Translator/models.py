from django.db import models
from django.contrib.auth.models import User

class Translation(models.Model):
    user = models.ForeignKey(User)
    #TODO: fix the max length limit
    sourceText = models.CharField(max_length=500)
    translatedText = models.CharField(max_length=500)
    
    @classmethod
    def create(cls, user, sourceText, translatedText):
        translation = cls(user=user, sourceText=sourceText, translatedText=translatedText)
        return translation
