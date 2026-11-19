from rest_framework import serializers

from ..models import ScreeningResult


class ScreeningResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScreeningResult
        fields = [
            "id",
            "candidate",
            "job_position",
            "score",
            "strengths",
            "missing_skills",
            "recommendation",
            "summary",
            "raw_report",
            "generated_at",
        ]
        read_only_fields = fields
