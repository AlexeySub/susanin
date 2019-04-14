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
    return(lst)


def findWay(data):
    data = data['txtway'].split('<br/>')
    way = data[1] + '. ' + data[2] + '. '
    data = data[3].split('</li><li>')
    way = way + '. ' + data[0][26:] + ' ' + data[1] + ' Затем ' + data[2].replace('</li></ul>', '')
    way = way.replace(' км.', ' километров.')
    way = way.replace(' м,', ' метров,')
    way = way.replace('\n', '')
    way = way.replace(' ч ', 'час')
    return {'way': way.replace('мин.', 'минут')}



