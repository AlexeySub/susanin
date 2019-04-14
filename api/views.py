from functools import reduce

from django import views, http
from api.models import BusStop as bs
from api.serializers import BusStopSerializer
from rest_framework import generics, parsers, renderers
import api.func, re


class BusStop(generics.ListCreateAPIView):
    queryset = bs.objects.all()
    serializer_class = BusStopSerializer


class BSDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = bs.objects.all()
    serializer_class = BusStopSerializer


class CheckBusStop(views.View):
    def post(self, request):
        data = parsers.JSONParser().parse(request)
        return http.HttpResponse(renderers.JSONRenderer().render({'busStop':api.func.findStop(data, bs)}))


class CreateWay(views.View):
    def post(self, request):
        data = parsers.JSONParser().parse(request)
        repls = {' км.': ' киллометров', ' м,': ' метров,', '\n': ''}
        data=data['txtway'].split('<br/>')
        way = data[1] + '. ' + data[2] + '. '
        data = data[3].split('</li><li>')
        way = way + '. ' + data[0][27:] + ' ' + data[1] + 'Затем ' + data[2].replace('</li></ul>', '')
        way = way.replace(repls)
        return http.HttpResponse(renderers.JSONRenderer().render({'way':way.replace('мин.', 'минут')}))
