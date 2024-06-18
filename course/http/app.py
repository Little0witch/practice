from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

API_KEY = '142b10f69c31d5d2568bf55ac959aca3'

@app.route('/weather/<city>', methods=['GET'])
def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        return jsonify(response.json()), response.status_code
    except requests.exceptions.HTTPError as err:
        return jsonify({'error': str(err)}), response.status_code
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
