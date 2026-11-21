from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import InterviewQuestionSet
from ..serializers import InterviewQuestionSetSerializer


@api_view(["GET"])
def interview_question_set_detail(request, pk):
    try:
        question_set = InterviewQuestionSet.objects.get(pk=pk)
    except InterviewQuestionSet.DoesNotExist:
        return Response(
            {"error": "Interview question set not found."},
            status=status.HTTP_404_NOT_FOUND,
        )
    serializer = InterviewQuestionSetSerializer(question_set)
    return Response(serializer.data)


InterviewQuestionSetDetailView = interview_question_set_detail
