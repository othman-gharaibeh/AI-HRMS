from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import InterviewQuestionSet
from ..serializers import InterviewQuestionSetSerializer


class InterviewQuestionSetDetailView(APIView):
    def get(self, request, pk):
        try:
            question_set = InterviewQuestionSet.objects.get(pk=pk)
        except InterviewQuestionSet.DoesNotExist:
            return Response(
                {"error": "Interview question set not found."},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = InterviewQuestionSetSerializer(question_set)
        return Response(serializer.data)
