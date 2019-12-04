from rest_framework import serializers
from .models import Event, Review, Attendance

class EventSerializer(serializers.ModelSerializer):
    organizer = serializers.StringRelatedField(read_only=True)
    attendances = serializers.StringRelatedField(read_only=True , many=True)
    attendance_count = serializers.SerializerMethodField()

    class Meta:
        model =Event
        fields = '__all__'

    def get_attendance_count(self, object):
        return object.attendances.count()

class confirmAttendanceSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model= Attendance
        fields = '__all__'

class Reviewserializer(serializers.ModelSerializer):
    event = serializers.StringRelatedField(read_only=True)
    reviewer = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        fields ='__all__'