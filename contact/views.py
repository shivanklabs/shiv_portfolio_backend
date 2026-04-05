from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ContactSerializer

class ContactView(APIView):
    def post(self, request):
        serializer = ContactSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "success": True,
                "data": serializer.data,
                "message": "Message sent successfully"
            })

        return Response({
            "success": False,
            "data": serializer.errors,
            "message": "Validation failed"
        }, status=status.HTTP_400_BAD_REQUEST)
