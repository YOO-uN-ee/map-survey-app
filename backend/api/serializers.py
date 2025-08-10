from rest_framework import serializers
from .models import SurveyResponse, User

class SurveyResponseSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='user_id',
        queryset=User.objects.all()
    )

    validity = serializers.ChoiceField(
        choices=[
            "Can be answered",
            "Map doesn't contain information to answer the question",
        ],
        required=True
    )
    necessary = serializers.ChoiceField(
        choices=["yes", "no"],
        required=False, allow_null=True, allow_blank=True
    )
    map_count = serializers.ChoiceField(
        choices=["Single", "Multi"], required=True
    )
    spatial_relationship = serializers.ChoiceField(
        choices=["Border", "Distance", "Equal", "Orientation", "Intersect", "Within"],
        required=True
    )

    class Meta:
        model = SurveyResponse
        fields = [
            "user",
            "question_ref",
            "question_text",
            "map_count",
            "spatial_relationship",
            "answer",
            "validity",
            "necessary",
            "timestamp",
        ]
        read_only_fields = ["timestamp"]