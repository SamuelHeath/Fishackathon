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
                            {'lat': -32.25140037, 'lng': 115.70398597},
                            {'lat': -32.26969077, 'lng': 115.69917945},
                            {'lat': -32.26504594, 'lng': 115.68733482},
                            {'lat': -32.26877387, 'lng': 115.68461289},
                            {'lat': -32.27232995, 'lng': 115.69087853},
                            {'lat': -32.28796968, 'lng': 115.70310872},
                            {'lat': -32.30513474, 'lng': 115.70036214},
                            {'lat': -32.31019194, 'lng': 115.73005944},
                            {'lat': -32.35216551, 'lng': 115.74239283},
                            {'lat': -32.36586018, 'lng': 115.72993976},
                            {'lat': -32.36077031, 'lng': 115.72993976},
                            {'lat': -32.36077031, 'lng': 115.71181225},
                            {'lat': -32.37207971, 'lng': 115.71507382},
                            {'lat': -32.38019841, 'lng': 115.66872524},
                            {'lat': -32.26284785, 'lng': 115.66872524},
                            {'lat': -32.25140037, 'lng': 115.70398597},
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
