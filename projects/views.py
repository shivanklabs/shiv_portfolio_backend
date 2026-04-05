from rest_framework import generics
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer

class ProjectListView(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        queryset = Project.objects.all().order_by('-created_at')
        search = self.request.GET.get('search')

        if search:
            queryset = queryset.filter(title__icontains=search)

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response({
            "success": True,
            "data": serializer.data,
            "message": "Projects fetched successfully"
        })