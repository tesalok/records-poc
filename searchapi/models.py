import uuid
from django.db import models

# Create your models here.
'''This model is used to store the json country data''' 
# Create your models here.
class Records(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fips=models.IntegerField(blank=False)
    state=models.CharField(max_length=20, null=False)
    name=models.TextField(blank=False, null=False)

    class Meta:
        db_table = 'records'