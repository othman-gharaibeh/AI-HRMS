from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..serializers import ResumeSerializer


@api_view(["POST"])
def resume_create(request):
    serializer = ResumeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


ResumeCreateView = resume_create
