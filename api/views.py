from django import views, http
from api.models import BusStop as bs
from api.serializers import BusStopSerializer
from rest_framework import generics, parsers, renderers
import api.func


class BusStop(generics.ListCreateAPIView):
    queryset = bs.objects.all()
    serializer_class = BusStopSerializer


class BSDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = bs.objects.all()
    serializer_class = BusStopSerializer


class BusStopAround(views.View):
    def post(self, request):
        data = parsers.JSONParser().parse(request)
        lst = api.func.findStop(data, bs)
        return http.HttpResponse(renderers.JSONRenderer().render({'busStop': lst[min(lst.keys())]}))


class CreateWay(views.View):
    def post(self, request):
        data = parsers.JSONParser().parse(request)
        return http.HttpResponse(renderers.JSONRenderer().render(api.func.findWay(data)))


"""class CheckBusStop(views.View):
    def post(self, request):
        data = parsers.JSONParser().parse(request)
        lst = api.func.findStop(data, bs)
        rangeBus = min(lst.keys())
        if rangeBus <= 0.06:
            return http.HttpResponse(renderers.JSONRenderer().render({'busStop': lst[rangeBus]}))
        else:
            return http.HttpResponse(renderers.JSONRenderer().render({'busStop': 'None'}))
"""
