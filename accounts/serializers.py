from rest_framework import serializers
from .models import userProfile


class userProfileSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = userProfile
        fields = '__all__'