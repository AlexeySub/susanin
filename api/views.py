from django.shortcuts import render
from django import views, http
from api.models import BusStop as bs
from api.serializers import BusStopSerializer
from rest_framework import generics, parsers, renderers
from haversine import haversine
# Create your views here.


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
        busStopLaLte = bs.objects.filter(latitude__lte=data['latitude']).order_by('-latitude')[0:1].get()
        print(busStopLaLte.latitude)
        busStopLoLte = bs.objects.filter(longitude__lte=data['longitude']).order_by('-longitude')[0:1].get()
        print(busStopLoLte.longitude)
        busStopLaGte = bs.objects.filter(latitude__gte=data['latitude']).order_by('latitude')[0:1].get()
        print(busStopLaGte.latitude)
        busStopLoGte = bs.objects.filter(longitude__gte=data['longitude']).order_by('longitude')[0:1].get()
        print(busStopLoGte.longitude)
        lst.update({haversine((float(busStopLaLte.latitude), float(busStopLaLte.longitude)), (float(data['latitude']), float(data['longitude']))):busStopLaLte.busStopName})
        lst.update({haversine((float(busStopLoLte.latitude), float(busStopLoLte.longitude)), (float(data['latitude']), float(data['longitude']))):busStopLoLte.busStopName})
        lst.update({haversine((float(busStopLaGte.latitude), float(busStopLaGte.longitude)), (float(data['latitude']), float(data['longitude']))):busStopLoGte.busStopName})
        lst.update({haversine((float(busStopLoGte.latitude), float(busStopLoGte.longitude)), (float(data['latitude']), float(data['longitude']))):busStopLaGte.busStopName})
        print(lst[min(lst.keys())])
        return http.HttpResponse(renderers.JSONRenderer().render({'busStop':lst[min(lst.keys())]}))
