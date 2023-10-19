from rest_framework import serializers
from .models import UserProfile, Destination, Booking


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

    # Exemple d'ajout de champ calculé
    total_bookings = serializers.SerializerMethodField()

    def get_total_bookings(self, obj):
        return obj.booking_set.count()


class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    # Exemple d'ajout de validation personnalisée
    def validate_date(self, value):
        from datetime import date
        if value < date.today():
            raise serializers.ValidationError("La date de réservation ne peut pas être dans le passé.")
        return value
