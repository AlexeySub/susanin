from haversine import haversine

def findStop(data, model):
    lst = {}
    try:
        busStopLaLte = model.objects.filter(latitude__lte=data['latitude']).order_by('-latitude')[0:1].get()
        print(busStopLaLte.latitude)
        lst.update({haversine((float(busStopLaLte.latitude), float(busStopLaLte.longitude)),
                              (float(data['latitude']), float(data['longitude']))): busStopLaLte.busStopName})
    except:
        None
    try:
        busStopLoLte = model.objects.filter(longitude__lte=data['longitude']).order_by('-longitude')[0:1].get()
        print(busStopLoLte.longitude)
        lst.update({haversine((float(busStopLoLte.latitude), float(busStopLoLte.longitude)),
                              (float(data['latitude']), float(data['longitude']))): busStopLoLte.busStopName})
    except:
        None
    try:
        busStopLaGte = model.objects.filter(latitude__gte=data['latitude']).order_by('latitude')[0:1].get()
        print(busStopLaGte.latitude)
    except:
        None
    try:
        busStopLoGte = model.objects.filter(longitude__gte=data['longitude']).order_by('longitude')[0:1].get()
        print(busStopLoGte.longitude)
        lst.update({haversine((float(busStopLoGte.latitude), float(busStopLoGte.longitude)),
                              (float(data['latitude']), float(data['longitude']))): busStopLaGte.busStopName})
    except:
        None
    try:
        lst.update({haversine((float(busStopLaGte.latitude), float(busStopLaGte.longitude)),
                              (float(data['latitude']), float(data['longitude']))): busStopLoGte.busStopName})
    except:
        None
    if min(lst.keys()) <= 0.015:
        return(lst[min(lst.keys())])
    else:
        return None