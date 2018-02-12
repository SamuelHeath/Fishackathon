from django.shortcuts import render
import json
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
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

class EquipmentListView(APIView):
    def get(self, requet, format=None):
        return JsonResponse(
            {
            'equipment': {
                'zone-0': [
                    {'name': 'Crab Pot'},
                    {'name': 'Fishing Net'},
                ],
                'zone-1': [
                    {'name': 'Crab Pot'},
                    {'name': 'TNT'},
                ],
            },
            }
        )

class LicencedZoneView(APIView):
    def get(self, request, format=None):

        zone_dic = { 'zone0': [
            'small boat',
            'trawler',
            'sailboat'
        ], 'zone1' : [ 
            'seaplane',
            'ship',
            'trawler'
        ], 'zone2' : [
            'speedboat',
            'medium boat',
            'trawler',
            'largeboat'
        ], 'zone3' : [
            'navy ship',
            'bulk carrier',
            'oil tanker',
            'car carrier'
        ]}

        zone_id = int(request.GET.get('zone-id'))

        return JsonResponse(
            {
                'legal_licences_for_zone' : zone_dic['zone{0}'.format(zone_id)]
            }
        )
