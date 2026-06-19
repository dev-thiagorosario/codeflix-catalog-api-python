from django.http import JsonResponse
from django.urls import include, path


def root(_request):
    return JsonResponse(
        {
            "name": "Codeflix Catalog API",
            "status": "running",
        }
    )


def health_check(_request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("", root, name="root"),
    path("health", health_check, name="health"),
    path("", include("django_prometheus.urls")),
]
