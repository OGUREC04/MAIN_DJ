import requests
import json
import polyline
import folium

m = folium.Map(location=[45.2, 121.2])

route_url = 'http://router.project-osrm.org/route/v1/driving/79.81039,12.00679;80.28150,13.08195?alternatives=true&geometries=polyline'
r = requests.get(route_url)
res = r.json()


def get_route(pickup_lon, pickup_lat, dropoff_lon, dropoff_lat):
    loc = "{},{};{},{}".format(pickup_lon, pickup_lat, dropoff_lon, dropoff_lat)
    url = "http://router.project-osrm.org/route/v1/driving/"
    r = requests.get(url + loc)
    if r.status_code != 200:
        return {}
    res = r.json()
    routes = polyline.decode(res['routes'][0]['geometry'])
    start_point = [res['waypoints'][0]['location'][1], res['waypoints'][0]['location'][0]]
    end_point = [res['waypoints'][1]['location'][1], res['waypoints'][1]['location'][0]]
    distance = res['routes'][0]['distance']

    out = {'route': routes,
           'start_point': start_point,
           'end_point': end_point,
           'distance': distance
           }

    return print(out)

get_route(44.2,44.3,44.4,44.5)