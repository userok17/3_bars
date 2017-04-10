import json
import math
import os
import sys
from pprint import pprint


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
    ''' Самый ближайший бар '''
    return min(data, key=lambda item: distance(item, longitude, latitude))


def ask_json_data(question):
    ''' Спросить путь до файла и вернуть json данные '''
    answer = None
    while True:
        answer = input(question)
        if answer == 'q':
            sys.exit(0)
        json_data = load_data(answer)
        if json_data:
            return json_data
        else:
            print('Путь до json файла указан не правильно. Попробуйте ввести снова.')

def ask_coordinate(question):
    ''' Спросить координаты '''
    while True:
        answer = input(question)
        if answer == 'q':
            sys.exit(0)
        try:
            answer = float(answer)
        except ValueError:
            print('Неправильно указано значение координата. Попробуйте заново.')
        else:
            return answer
    

def print_bar(json_data):
        ''' Вывести информацию о баре '''
        print('Название бара: {}'.format(json_data['Name']))
        print('Адрес: {}'.format(json_data['Address']))
        print('Количество мест: {}'.format(json_data['SeatsCount']))
        print()
    
def main():
    print('Программа Бары!\n')
    
    json_data = ask_json_data('Введите путь до json файла или "q" для выхода из программы: ')
    
    longitude = ask_coordinate('Введите долготу c gps-координаты или "q" для выхода из программы: ')
    latitude = ask_coordinate('Введите широту c gps-координаты или "q" для выхода из программы: ')
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
    
