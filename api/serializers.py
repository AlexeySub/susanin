from rest_framework import serializers
from api.models import BusStop


class BusStopSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusStop
        fields = ('busStopName', 'latitude', 'longitude')