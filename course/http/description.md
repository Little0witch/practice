Условие задачи: Необходимо получить все статусы ответов. Если у Вас ранее был опыт написания сервера, то Вам необходимо
написать свой сервер и используя API получить все статусы ответов. 
Ссылка на API. (https://openweathermap.org/api)
В файле z1.py для решения поставленной задачи применена библиотека requests. При ее помощи получены статус успешного запроса и статус ошибки клиента.
Были использованый ззапросы: get, head. 
При использовании данных методов получены статусы:
- 200 - Запрос успешно выполнен.
- 400 - Сервер не может или не будет обрабатывать запрос из-за чего-то, что воспринимается как ошибка клиента (например, неправильный синтаксис, формат или маршрутизация запроса). В запросе я указала неверное значения lat.
- 401 - Хотя стандарт HTTP определяет этот ответ как «неавторизованный», семантически он означает «неаутентифицированный». Это значит, что клиент должен аутентифицировать себя, чтобы получить запрошенный ответ. При использования API на бесплатной основе есть ограничения в возможностях. Данный код получен в связи с тем, что была попытка обратиться к недоступному(платному) ресурсу.
- 404 - Сервер не может найти запрошенный ресурс. В браузере это означает, что URL-адрес не распознан. В запросе допущена ошибка: неверное написание (weathe).

В файле app.py написано второе решение поставленной задачи - создание сервера для обращения к API.
Реализовны два метода: get, delete. Получены три кода: 200, 404, 405.
- 405 - Метод запроса известен серверу, но не поддерживается целевым ресурсом. Например, API может не разрешать вызов DELETE для удаления ресурса.

Существует 5 классов состояний ответа HTTP:
- Информационные ответы (100 – 199). Сообщают о прогрессе выполнения запроса. На практике практически не встречаются.
- Успешные ответы (200 – 299). Сообщают о том, что всё в порядке и работает, как ожидалось.
- Сообщения о перенаправлении (300 – 399). Сообщают о том, что запрашиваемая страница переехала и нужно сделать ещё один запрос по новому URL.
- Ошибки клиента (400 – 499). Сообщают об ошибке на стороне пользователя, который отправил запрос.
- Ошибки сервера (500 – 599). Сообщают об ошибке на стороне сервера, который обрабатывал запрос.
