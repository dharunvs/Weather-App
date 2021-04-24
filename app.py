import os
import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv
load_dotenv()

app = Flask(
        __name__,
        template_folder="./client/templates",
        static_folder="./client/static"
    )

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('API_KEY')}"
    weather_details = requests.get(url).json()
    return {
        "description" : weather_details["weather"][0]["description"],
        "temp": weather_details['main']['temp'],
    }

@app.route('/', methods=['GET', 'POST'])
def weather():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        location = request.form['city']
        data = get_weather(location)
        return render_template(
            'index.html',
            city=location,
            temp = data['temp'],
            desc=data['description'])

    
if __name__ == "__main__":
    app.run(debug=True)