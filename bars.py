import json
import math
import os

def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, encoding='windows-1251') as data_file:
        return json.load(data_file)


    

def get_biggest_bar(json_data):
    dict_bar = max(json_data, key=lambda item: item['SeatsCount'])
    return dict_bar


def get_smallest_bar(json_data):
    dict_bar = min(json_data, key=lambda item: item['SeatsCount'])
    return dict_bar


def get_closest_bar(data, longitude, latitude):
    return min(data, key=lambda item: math.sqrt((longitude - float(item['Longitude_WGS84']))**2 + (latitude - float(item['Latitude_WGS84']))**2))


if __name__ == '__main__':
    json_data = load_data('data-2897-2016-11-23.json')
    print(get_biggest_bar(json_data))
    print(get_smallest_bar(json_data))
    print(get_closest_bar(json_data, 37.6215879462381080, 55.7653669567739740))
