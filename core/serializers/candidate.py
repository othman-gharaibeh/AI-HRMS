from rest_framework import serializers

from ..models import Candidate


class CandidateSerializer(serializers.ModelSerializer):
    def validate_phone(self, value):
        numbers = value[1:] if value.startswith("+") else value
        if not numbers or any(char not in "0123456789" for char in numbers):
            raise serializers.ValidationError("Phone number must contain only + and numbers.")
        if len(numbers) < 7 or len(numbers) > 15:
            raise serializers.ValidationError(
                "Phone number must contain between 7 and 15 digits."
            )

        return value

    class Meta:
        model = Candidate
        fields = ["id", "full_name", "email", "phone", "created_at"]
        read_only_fields = ["id", "created_at"]
