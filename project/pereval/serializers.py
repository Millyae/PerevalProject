from rest_framework import serializers
from .models import Users, Coords, PerevalAdded, PerevalImage

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['email', 'phone', 'fam', 'name', 'otc']

class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ['latitude', 'longitude', 'height']

class PerevalImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalImage
        fields = ['img', 'title']

class PerevalAddedSerializer(serializers.ModelSerializer):
    coord = CoordsSerializer()
    images = PerevalImageSerializer(many=True, read_only=True)

    class Meta:
        model = PerevalAdded
        fields = ['date_added', 'beauty_title', 'title', 'other_titles', 'connect', 'add_time', 'coord', 'level_winter', 'level_summer', 'level_autumn', 'level_spring', 'images']