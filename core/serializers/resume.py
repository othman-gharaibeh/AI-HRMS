from pathlib import Path

from rest_framework import serializers

from ..models import Resume


class ResumeSerializer(serializers.ModelSerializer):
    MAX_RESUME_SIZE = 5 * 1024 * 1024

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
        if value.size > self.MAX_RESUME_SIZE:
            raise serializers.ValidationError(
                "Resume file size cannot exceed 5 MB."
            )
        return value
