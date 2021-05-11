
import requests
import configparser
from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def weather_dashboard():
    return render_template('index.html')

@app.route('/result', methods=['GET','POST'])
def render_results():
    city=request.form['city']
    api_key= get_api_key()
    data=get_weather(city,api_key)
    temp="{0:2f}".format(data["main"]["temp"])
    feels_like=data["main"]["feels_like"]
    weather=data["weather"][0]["main"]
    location=data["name"]
    return render_template('result.html',location=location,temp=temp,feels_like=feels_like,weather=weather)

def get_api_key():
    config=configparser.ConfigParser()
    config.read('config.ini')
    return config['weatherproject']['api']

def get_weather(city,api_key):
    api_url="http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(city,api_key)
    j=requests.get(api_url)
    return j.json()
if __name__ == "__main__":
    app.run(debug=True)



