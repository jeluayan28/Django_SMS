from django.db import models
from twilio.rest import Client

class Message(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    def send_sms(self):
        account_sid = 'AC4e346e0ca8490da69d91efa73a856ddd'
        auth_token = '2ac7a6321b9ac774372e4511c28cc359'
        client = Client(account_sid, auth_token)

        if self.score >= 70:
            message_body = f"Hi {self.name}, your score is {self.score}. Congratulations, you passed!"
        else:
            message_body = f"Hi {self.name}, your score is {self.score}. Unfortunately, you failed."

        message = client.messages.create(
            body=message_body,
            from_='+19787562664', 
            to='+639382326740',    
        )

        print(f"Message sent with SID: {message.sid}")
    
    def save(self, *args, **kwargs):
        self.send_sms()

        return super().save(*args, **kwargs)
