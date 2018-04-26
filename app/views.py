from django.http import JsonResponse


def f():
    return JsonResponse({"message": "Requested a view!"})