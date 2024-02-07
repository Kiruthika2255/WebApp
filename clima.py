from flask import Flask, render_template
from temp import get_temperature
import os

app = Flask(__name__)

@app.route('/weather')
def weather_main():
    temp, temp_min, temp_max = get_temperature()
    img_name = os.listdir('static1/images')[0]  # Assuming there's only one image in the directory
    return render_template('index.html', city_temp=temp, city_min_temp=temp_min, city_max_temp=temp_max, temp_img=img_name)

@app.route('/cat')
def cat_main():
    return 'Welcome'

if __name__ == '__main__':
    app.run(port=1010)
