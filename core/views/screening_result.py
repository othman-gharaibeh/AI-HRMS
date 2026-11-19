from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import ScreeningResult
from ..serializers import ScreeningResultSerializer


class ScreeningResultDetailView(APIView):
    def get(self, request, pk):
        try:
            screening_result = ScreeningResult.objects.get(pk=pk)
        except ScreeningResult.DoesNotExist:
            return Response(
                {"error": "Screening result not found."},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = ScreeningResultSerializer(screening_result)
        return Response(serializer.data)
