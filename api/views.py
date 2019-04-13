from django.shortcuts import render
from django import views, http
from api.models import BusStop as bs
from api.serializers import BusStopSerializer
from rest_framework import generics, parsers, renderers
from haversine import haversine
import api.mapoutputparser as mp


class BusStop(generics.ListCreateAPIView):
    queryset = bs.objects.all()
    serializer_class = BusStopSerializer


class BSDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = bs.objects.all()
    serializer_class = BusStopSerializer


class CheckBusStop(views.View):
    def post(self, request):
        data = parsers.JSONParser().parse(request)
        lst = {}

        try:
            busStopLaLte = bs.objects.filter(latitude__lte=data['latitude']).order_by('-latitude')[0:1].get()
            print(busStopLaLte.latitude)
            lst.update({haversine((float(busStopLaLte.latitude), float(busStopLaLte.longitude)),
                                  (float(data['latitude']), float(data['longitude']))): busStopLaLte.busStopName})
        except:
            None
        try:
            busStopLoLte = bs.objects.filter(longitude__lte=data['longitude']).order_by('-longitude')[0:1].get()
            print(busStopLoLte.longitude)
            lst.update({haversine((float(busStopLoLte.latitude), float(busStopLoLte.longitude)),
                              (float(data['latitude']), float(data['longitude']))): busStopLoLte.busStopName})
        except:
            None
        try:
            busStopLaGte = bs.objects.filter(latitude__gte=data['latitude']).order_by('latitude')[0:1].get()
            print(busStopLaGte.latitude)
        except:
            None
        try:
            busStopLoGte = bs.objects.filter(longitude__gte=data['longitude']).order_by('longitude')[0:1].get()
            print(busStopLoGte.longitude)
            lst.update({haversine((float(busStopLoGte.latitude), float(busStopLoGte.longitude)),
                                  (float(data['latitude']), float(data['longitude']))):busStopLaGte.busStopName})
        except:
            None
        try:
            lst.update({haversine((float(busStopLaGte.latitude), float(busStopLaGte.longitude)),
                                  (float(data['latitude']), float(data['longitude']))): busStopLoGte.busStopName})
        except:
            None
        print(lst[min(lst.keys())])
        return http.HttpResponse(renderers.JSONRenderer().render({'busStop':lst[min(lst.keys())]}))


class CreateWay(views.View):
    def post(self, request):
        data = parsers.JSONParser().parse(request)
        print(data['txtway'])
        data=data['txtway'].split('<br/>')
        way = data[1] + '. ' + data[2] + '. '
        data = data[3].split('</li><li>')
        way = way + '. Пешком до остановки ' + data[0][39:].replace('\n', '') + ' ' + data[1].replace('\n', '') + 'Затем пешком ' + data[2].replace('</li></ul>', '')
        way = way.replace(' км.', ' километров.')
        way = way.replace(' м,', ' метров,')
        return http.HttpResponse(renderers.JSONRenderer().render({'way':way.replace('мин.', 'минут')}))
