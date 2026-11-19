from rest_framework import serializers

from ..models import InterviewQuestionSet


class InterviewQuestionSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewQuestionSet
        fields = [
            "id",
            "candidate",
            "job_position",
            "screening_result",
            "technical_questions",
            "behavioral_questions",
            "follow_up_questions",
            "generated_at",
        ]
        read_only_fields = fields
