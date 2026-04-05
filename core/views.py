from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "message": "Backend is running 🚀",
        "endpoints": [
            "/api/v1/projects/",
            "/api/v1/blog/",
            "/api/v1/contact/"
        ]
    })