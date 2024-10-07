from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    if not bool(city.strip()):
        city = "Houston"
    weather_data = get_current_weather(city)
    # if the city search provided no data
    if weather_data ==[]:
        return render_template('city-not-found.html')


    return render_template(
        "weather.html",
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{((weather_data['main']['temp']-273.15)*9/5 + 32):.1f}",
        feels_like=f"{((weather_data['main']['feels_like']-273.15)*9/5 + 32):.1f}"
    )


if __name__ == "__main__":
    print("Starting the server on http://127.0.0.1:8000")
    serve(app, host="0.0.0.0", port=8000)
