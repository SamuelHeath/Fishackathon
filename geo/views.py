import json

class EquipmentView(APIView):
    def get(self, request, format=None):
        zone_id = request.GET.get('zone-id')
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
                    {},
                    ]
                    }
                )
