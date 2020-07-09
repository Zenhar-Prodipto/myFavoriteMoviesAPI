from rest_framework import serializers
from .models import Movie

class serializerClass(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("id","name","director","release_date","imdb_rating","timestamp_of_imdb")