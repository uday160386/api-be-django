from rest_framework import serializers

from app.models import Medicines


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicines
        fields = ('title', 'description', 'qty')