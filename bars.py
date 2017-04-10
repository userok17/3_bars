import json
import math
import os
import sys

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


def distance(item, longitude, latitude):
    return math.sqrt((longitude - float(item['Longitude_WGS84']))**2 + (latitude - float(item['Latitude_WGS84']))**2)
    

def get_closest_bar(data, longitude, latitude):
    return min(data, key=lambda item: distance(item, longitude, latitude))


def ask(question, type_value=str):
    answer = input(question)
    if not answer:
        print('Ошибка: Значение не может быть пустым')
        sys.exit(1)        
    try:
        answer = type_value(answer)
    except ValueError:
        print('Ошибка: Неправильно указано значение.')
        sys.exit(1)
    return answer

    
        
def print_bar(json_data):
    print('Название бара: {}'.format(json_data['Name']))
    print('Адрес: {}'.format(json_data['Address']))
    print('Количество мест: {}'.format(json_data['SeatsCount']))
    print()
    
def main():
    print('Программа Бары!\n')
    
    filepath = ask(question='Введите путь до json файла: ')
    json_data = load_data(filepath)
    
    if not json_data:
        print('Ошибка: Путь до json файла указан не правильно.')
        sys.exit(0)
    
    longitude = ask(question='Введите долготу c gps-координаты: ', type_value=float)
    latitude = ask(question='Введите широту c gps-координаты: ', type_value=float)
    
    print()
    
    print('Самый маленький бар:')
    the_smallest_bar = get_smallest_bar(json_data)
    print_bar(the_smallest_bar)

    print('Самый большой бар:')
    the_biggest_bar = get_biggest_bar(json_data)
    print_bar(the_biggest_bar)

    print('Самый ближайший бар:')
    the_closest_bar = get_closest_bar(json_data, longitude, latitude)    
    print_bar(the_closest_bar)

if __name__ == '__main__':
    main()
    
