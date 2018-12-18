from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Software
from .models import Programming
from .models import Question
from .models import Opensource
from .models import Experience
from .models import Post
User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class SoftwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Software
        fields = "__all__"


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programming
        fields = "__all__"


class OpensourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opensource
        fields = "__all__"


class ExperienceSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Experience
        fields = ("user", "id", "title", "description")


class QuestionSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Question
        fields = ("user", "id", "title", "description")


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        depth = 2


