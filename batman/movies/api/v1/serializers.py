from movies.models import Cast, Movies, Villain
from rest_framework import serializers


class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = (
            "name",
            "birthday",
            "demise",
            "height",
        )


class VillainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Villain
        fields = (
            "name",
            "birthday",
            "demise",
            "height",
        )


class MoviesSerializer(serializers.ModelSerializer):
    casts = CastSerializer(many=True, read_only=True)
    villains = VillainSerializer(many=True, read_only=True)

    class Meta:
        model = Movies
        fields = [
            "title",
            "main_actor",
            "director",
            "casts",
            "villains",
            "summary",
            "published",
        ]
