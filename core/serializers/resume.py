from pathlib import Path

from rest_framework import serializers

from ..models import Resume


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ["id", "candidate", "file", "uploaded_at"]
        read_only_fields = ["id", "uploaded_at"]

    def validate_file(self, value):
        extension = Path(value.name).suffix.lower()
        if extension not in {".pdf", ".docx", ".txt"}:
            raise serializers.ValidationError(
                "Unsupported file extension. Allowed extensions: .pdf, .docx, .txt."
            )
        return value
