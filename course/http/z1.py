import requests

# # 200
# print(requests.get("https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=142b10f69c31d5d2568bf55ac959aca3"))
# # 400
# print(requests.get("https://api.openweathermap.org/data/2.5/weather?lat=-&lon=10.99&appid=142b10f69c31d5d2568bf55ac959aca3"))
# # 401
# print(requests.get("https://api.openweathermap.org/data/3.0/onecall/timemachine?&appid=627a64002a11e33bbea79bcb3c7ab7a2"))
# # 404
# print(requests.get("https://api.openweathermap.org/data/2.5/weathe?lat=-&lon=10.99&appid=142b10f69c31d5d2568bf55ac959aca3"))
#
# # 200
# print(requests.head("https://api.openweathermap.org/data/2.5/weather?q=London&appid=142b10f69c31d5d2568bf55ac959aca3"))
# # 404
# print(requests.head("https://api.openweathermap.org/data/2.5/weathe?q=London&appid=142b10f69c31d5d2568bf55ac959aca3"))

# from flask import Flask, jsonify
# import requests
#
# app = Flask(__name__)
#
# @app.route('/weather')
# def get_weather():
#     api_key = '142b10f69c31d5d2568bf55ac959aca3'  # Вставьте ваш API-ключ OpenWeatherMap
#     url = 'https://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=' + api_key
#
#     response = requests.get(url)
#     status_code = response.status_code
#
#     return jsonify({'status_code': status_code})
#
# if __name__ == '__main__':
#     app.run()

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=142b10f69c31d5d2568bf55ac959aca3', 8000)) # Подключаемся к нашему серверу.
s.sendall('Hello, Habr!'.encode('utf-8')) # Отправляем фразу.
data = s.recv(1024) #Получаем данные из сокета.
s.close()
