from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from .models import *
from django.db.models.functions import Length


class fieldsAmbito(APIView):
    def get(self, request, nivel):
        campos = camposReporte.objects.filter(nivel_id=nivel).values().order_by('pk')
        return JsonResponse(list(campos), safe=False)
