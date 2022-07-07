from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import APIKeys
from .serializer import APIKeySerializer
from django.shortcuts import get_object_or_404

# Create your views here.


# creating and displaying all keys
@api_view(http_method_names=["GET", "POST"])
def keyList(request: Response):
    keys = APIKeys.objects.all()

    if request.method == "POST":
        data = request.data
        serializer = APIKeySerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {"message": "APIKeys Created", "data": serializer.data}
            return Response(data=response, status=status.HTTP_201_CREATED)
        # for invalid data
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # APIKeyss.Objects returns a queryset and many=True converts that to a list fromat
    serializer = APIKeySerializer(instance=keys, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(http_method_names=["DELETE"])
def keyDelete(request: Request, key_id):
    key = get_object_or_404(APIKeys, pk=key_id)
    key.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
