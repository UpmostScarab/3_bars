import json

def distance(x1,y1,x2,y2):
    return (x1 - x2)**2 + (y1 - y2)**2


def load_data(filepath):
    with open(filepath) as file:
        bars = json.loads(file.read())
    return bars


def get_biggest_bar(data):
    return max(bars, key = lambda x: x['Cells']['SeatsCount'])


def get_smallest_bar(data):
    return min(bars, key = lambda x: x['Cells']['SeatsCount'])

def get_closest_bar(data, longitude, latitude):
    return min(bars, key = lambda x: \
        distance(*x['Cells']['geoData']['coordinates'], longitude, latitude))


if __name__ == '__main__':
    bars = load_data('bars.json')
    print('Самый большой бар:',get_biggest_bar(bars))
    print('Самый маленький бар: ',get_smallest_bar(bars))
    lat = float(input('Введите широту: '))
    lon = float(input('Введите долготу: '))
    print("Самый близкий бар",get_closest_bar(bars, lon, lat))
