import json


def load_data(filepath):
    with open(filepath) as file:
        bars = json.loads(file.read())
    return bars


def get_biggest_bar(data):
    return max(bars, key = lambda x: x['Cells']['SeatsCount'])


def get_smallest_bar(data):
    return min(bars, key = lambda x: x['Cells']['SeatsCount'])

def get_closest_bar(data, longitude, latitude):
    return min(bars, key = lambda x: (x['Cells']['geoData']['coordinates'][0] - longitude)**2  + (x['Cells']['geoData']['coordinates'][1] - latitude)**2)


if __name__ == '__main__':
    bars = load_data('bars.json')
    print(get_biggest_bar(bars))
    print(get_smallest_bar(bars))
    lat = float(input('Введите широту: '))
    lon = float(input('Введите долготу: '))
    print(get_closest_bar(bars, lon, lat))
