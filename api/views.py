from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from agent_dashboard.models import Property
from agent_dashboard.serializers import PropertySerializer
from django.template.loader import render_to_string

# Create your views here.

@api_view(['GET'])
def property_list(request):
    properties = Property.objects.all()
    serializer = PropertySerializer(properties, many=True)
    return Response(serializer.data)

def property_details(request, property_id):
    try:
        property_instance = Property.objects.get(id=property_id)
        serializer = PropertySerializer(property_instance)
        return JsonResponse(serializer.data, status=200)
    except Property.DoesNotExist:
        return JsonResponse({"error": "Property not found"}, status=404)