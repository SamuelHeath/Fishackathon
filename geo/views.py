from rest_framework.views import APIView
from django.http import JsonResponse

def index(request):
    return 

class RestrictedZoneView(APIView):
    def get(self, request, format=None):
        return JsonResponse(
            {
                'zones': [
                    {
                        'id': 0,
                        'points': [
                            {'lat': 110, 'lng': 110},
                            {'lat': 110, 'lng': 111},
                            {'lat': 109, 'lng': 110},
                            {'lat': 119, 'lng': 111},
                        ]
                    },
                    {
                        'id': 1,
                        'points': [
                            {'lat': 110, 'lng': 110},
                            {'lat': 110, 'lng': 111},
                            {'lat': 109, 'lng': 110},
                            {'lat': 119, 'lng': 111},
                        ]
                    },
                ]
            }
        )

class EquipmentView(APIView):
    def get(self, request, format=None):
        zone_id = int(request.GET.get('zone-id'))
        if zone_id == 0:
            return JsonResponse(
                {
                'equipment': [
                    {
                    'name': 'Crab Pot',
                        },
                    {'name': 'Fishing Net'},
                ]
                }
            )
        elif zone_id == 1:
            return JsonResponse(
                {
                'equipment': [
                    {'name': 'Crab Pot'},
                    {'name': 'TNT'},
                ]
                }
            )
        else:
            return JsonResponse(
                {
                'equipment': []
                }    
            )
