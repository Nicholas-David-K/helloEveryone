from rest_framework import serializers
from taifa.models import Ebook, Review


class ReviewSerializer(serializers.ModelSerializer):
    ebook = serializers.StringRelatedField()
    review_author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = "__all__"



class EbookSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Ebook
        fields = "__all__"


