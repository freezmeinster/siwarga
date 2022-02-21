from django.http import JsonResponse
from .models import Warga

def list_warga(request):
    list_warga = []
    for warga in Warga.objects.all():
        list_warga.append({
            "nama": warga.name,
            "dob": warga.dob,
            "address": warga.address
        })
    result = {
        "data": list_warga
    }
    return JsonResponse(result)

