
import json

end_point = 'https://api.openweathermap.org/data/2.5/weather?q=Chennai&appid=be1794c985848893d0b272cf3e2e2244&units=metric'

def get_temperature():
    response = requests.get(end_point)
    dict_response = json.loads(response.text)
    return dict_response['main']['temp'], dict_response['main']['temp_min'], dict_response['main']['temp_max']


