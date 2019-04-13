from django import views, http
from api.models import BusStop as bs
from api.serializers import BusStopSerializer
from rest_framework import generics, parsers, renderers
from haversine import haversine
import api.func


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
        print(data['txtway'])
        data=data['txtway'].split('<br/>')
        way = data[1] + '. ' + data[2] + '. '
        data = data[3].split('</li><li>')
        way = way + '. ' + data[0][27:].replace + ' ' + data[1] + 'Затем пешком ' + data[2].replace('</li></ul>', '')
        way = way.replace(' км.', ' километров.')
        way = way.replace(' м,', ' метров,')
        way = way.replace('\n', 'n')
        return http.HttpResponse(renderers.JSONRenderer().render({'way':way.replace('мин.', 'минут')}))
