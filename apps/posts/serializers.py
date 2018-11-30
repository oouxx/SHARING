from rest_framework import serializers
from .models import Software
from users.models import UserProfile
from .models import SoftwareDetail


class SoftwareDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoftwareDetail
        fields = "__all__"


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


class SoftwareSerializer(serializers.ModelSerializer):
    release_person= UserProfileSerializer()
    contribute_person= UserProfileSerializer()
    detail = SoftwareDetailSerializer()

    class Meta:
        model = Software
        fields = "__all__"

