from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import ScreeningResult
from ..serializers import ScreeningResultSerializer


@api_view(["GET"])
def screening_result_detail(request, pk):
    try:
        screening_result = ScreeningResult.objects.get(pk=pk)
    except ScreeningResult.DoesNotExist:
        return Response(
            {"error": "Screening result not found."},
            status=status.HTTP_404_NOT_FOUND,
        )
    serializer = ScreeningResultSerializer(screening_result)
    return Response(serializer.data)


ScreeningResultDetailView = screening_result_detail
