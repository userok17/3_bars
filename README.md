# Ближайшие бары

На сайте data.mos.ru есть много разных данных, в том числе список московских баров. Его можно скачать в формате json.

Требуется написать скрипт, который рассчитает:

    самый большой бар;
    самый маленький бар;
    самый близкий бар (текущие gps-координаты ввести с клавиатуры).


# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```#!bash

$ python bars.py # possibly requires call of python3 executive instead of just python
{'Latitude_WGS84': '55.7011146292467670', 'PublicPhone': [{'global_id': 33761.0, 'PublicPhone': '(905) 795-15-84', 'global_object_id': 169375059.0, 'system_object_id': '00138530 _1'}], 'system_object_id': '00138530', 'AdmArea': 'Южный административный округ', 'Name': 'Спорт бар «Красная машина»', 'geoData': {'coordinates': [37.638228501070095, 55.70111462948684], 'type': 'Point'}, 'SeatsCount': 450, 'TypeObject': 'бар', 'IsNetObject': 'нет', 'SocialPrivileges': 'нет', 'District': 'Даниловский район', 'global_id': 169375059, 'Longitude_WGS84': '37.6382285008039050', 'ID': '00138530', 'Address': 'Автозаводская улица, дом 23, строение 1'}
{'Latitude_WGS84': '55.8461447588834330', 'PublicPhone': [{'global_id': 22348.0, 'PublicPhone': '(495) 258-94-19', 'global_object_id': 20675518.0, 'system_object_id': '00107283 _1'}], 'system_object_id': '00107283', 'AdmArea': 'Северо-Западный административный округ', 'Name': 'БАР. СОКИ', 'geoData': {'coordinates': [37.35805920566864, 55.84614475898795], 'type': 'Point'}, 'SeatsCount': 0, 'TypeObject': 'бар', 'IsNetObject': 'нет', 'SocialPrivileges': 'нет', 'District': 'район Митино', 'global_id': 20675518, 'Longitude_WGS84': '37.3580592058223000', 'ID': '00107283', 'Address': 'Дубравная улица, дом 34/29'}
{'Latitude_WGS84': '55.7653669567739740', 'PublicPhone': [{'global_id': 21025.0, 'PublicPhone': '(495) 621-19-63', 'global_object_id': 20660594.0, 'system_object_id': '000069302_1'}], 'system_object_id': '000069302', 'AdmArea': 'Центральный административный округ', 'Name': 'Юнион Джек', 'geoData': {'coordinates': [37.62158794615201, 55.76536695660836], 'type': 'Point'}, 'SeatsCount': 30, 'TypeObject': 'бар', 'IsNetObject': 'нет', 'SocialPrivileges': 'нет', 'District': 'Мещанский район', 'global_id': 20660594, 'Longitude_WGS84': '37.6215879462381080', 'ID': '000069302', 'Address': 'Нижний Кисельный переулок, дом 3, строение 1'}

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
