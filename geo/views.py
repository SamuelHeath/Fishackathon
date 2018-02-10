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
                            {'lattitude': 110, 'longitude': 110},
                            {'lattitude': 110, 'longitude': 111},
                            {'lattitude': 109, 'longitude': 110},
                            {'lattitude': 119, 'longitude': 111},
                        ]
                    },
                    {
                        'id': 1,
                        'points': [
                            {'lattitude': 110, 'longitude': 110},
                            {'lattitude': 110, 'longitude': 111},
                            {'lattitude': 109, 'longitude': 110},
                            {'lattitude': 119, 'longitude': 111},
                        ]
                    },
                ]
            }
        )
