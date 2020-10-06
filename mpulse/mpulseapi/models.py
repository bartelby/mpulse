from django.db import models

# Note <li>Django adds an auto-incrementing id field to each model by default.
#     <li>The format of member and account id fields is not specified. Validators can be provided for these fields if required. 
class Member(models.Model):
    first_name=models.CharField(max_length=64)
    last_name=models.CharField(max_length=64)
    phone_number=models.CharField(max_length=32)
    client_member_id=models.CharField(max_length=32)
    account_id=models.CharField(max_length=32) #ASSUMPTION: This is the healthcare provider account ID.

    class Meta:
        constraints = [
                models.UniqueConstraint(fields=['phone_number', 'account_id'], name='unique_phone_number'),
                models.UniqueConstraint(fields=['client_member_id', 'account_id'], name='unique_member_id'),
            ]

    def __str__(self):
        return ", ".join([self.last_name, self.first_name])
