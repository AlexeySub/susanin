from django.urls import path, include
from api import views


urlpatterns = [
    path('busstops/', views.BusStop.as_view()),
    path('busstops/<int:pk>/', views.BSDetail.as_view()),
    path('busaround/', views.BusStopAround.as_view()),
    #path('checkbus/', views.CheckBusStop.as_view()),
    path('way/', views.CreateWay.as_view()),
    #path('save/', views.SaveBusStop.as_view())
]