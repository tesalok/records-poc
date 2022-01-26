
from rest_framework import serializers

from searchapi.models import Records


'''List the Records created'''

class RecordSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Records
        fields=('fips','state','name')

