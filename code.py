import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return "Could not fetch weather."

if __name__ == "__main__":
    city = input("Enter city name: ")
    print(get_weather(city))
