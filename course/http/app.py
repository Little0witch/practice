from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

API_KEY = '142b10f69c31d5d2568bf55ac959aca3'

# моделирует 200 и 404
@app.route('/weather/<city>', methods=['GET'])
def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    try:
        response = requests.get(url)
        return jsonify(response.json()), response.status_code
    except requests.exceptions.HTTPError as err:
        return jsonify({'error': str(err)}), response.status_code

# моделирует 405
@app.route('/weather', methods=['DELETE'])
def delete_weather():
    url = f'http://api.openweathermap.org/data/2.5/weather?appid={API_KEY}'
    try:
        response = requests.delete(url)
        return jsonify(response.json()), response.status_code
    except requests.exceptions.HTTPError as err:
        return jsonify({'error': str(err)}), response.status_code


if __name__ == '__main__':
    app.run(debug=True, port=5000)
