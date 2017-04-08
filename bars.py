import json
import math

def load_data(filepath):
    with open(filepath, encoding='windows-1251') as data_file:
        return json.load(data_file)


    

def get_biggest_bar(data):
    dict_bar = max(data, key=lambda item: item['SeatsCount'])
    return dict_bar['SeatsCount']


def get_smallest_bar(data):
    dict_bar = min(data, key=lambda item: item['SeatsCount'])
    return dict_bar['SeatsCount']


def get_closest_bar(data, longitude, latitude):
    return min(data, key=lambda item: math.sqrt((longitude - float(item['Longitude_WGS84']))**2 + (latitude - float(item['Latitude_WGS84']))**2))


if __name__ == '__main__':
    data = load_data('data-2897-2016-11-23.json')
    print(get_biggest_bar(data))
    print(get_smallest_bar(data))
    print(get_closest_bar(data, 37.6215879462381080, 55.7653669567739740))
