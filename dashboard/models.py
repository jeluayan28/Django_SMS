from django.db import models
from twilio.rest import Client

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.score >=70:
            account_sid = 'AC0b14ddf4dc39e5cf20cf66212d4ea91c'
            auth_token = '5286644fc2a8bdef7299de11be411483'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f"Hi {self.name}, your score is {self.score} Thank you!",
                from_="+17753709175",
                to="+639073042157",
            )


            print(message.sid)

        return super().save(*args, **kwargs)
