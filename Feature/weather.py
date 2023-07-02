import requests

def get_weather_data(Your_current_State, API_Key):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={Your_current_State}&appid={API_Key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
