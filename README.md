<h1> Проект по тестированию сайта Litres</h1>

> <a target="_blank" href="https://www.litres.ru/">Ссылка на сайт</a>

![Homepage](./litres/image/Homepage.png)

### Список проверок:
* Поиск книг по названию или автору
* Добавление книги в Отложенные
* Удаление книги из Отложенных товаров
* Добавление книги в корзину
* Удаление книги из корзины 

### Особенности проекта:
* Проверки проводятся для неавторизованного пользователя
* В телеграм приходят оповещения о результатах прохождения тестов
* Сборка проекта осуществляется через Jenkins 
* Отчеты в Allure Report
----

### Используемый стэк

<img title="Python" src="./litres/image/python.png" height="40" width="40"/> <img title="Pytest" src="./litres/image/pytest.png" height="40" width="40"/> <img title="Pycharm" src="./litres/image/pycharm.png" height="40" width="40"/> <img title="Jenkins" src="./litres/image/jenkins.png" height="40" width="40"/> <img title="GitHub" src="./litres/image/github.png" height="40" width="40"/> <img title="Allure Report" src="./litres/image/allure_report.png" height="40" width="40"/> <img title="Allure TestOps" src="./litres/image/allureTestOps.png" height="40" width="40"/><img title="Telegram" src="./litres/image/telegram.png" height="40" width="40"/> 

----

### Проект в Jenkins
> <a target="_blank" href="https://github.com/Annatrg/litres">Ссылка на проект в Jenkins</a>

Наш проект возможно запускать через Jenkins. Доступны следующие параметры сборки:
* `environment` - параметр позволяет выбрать окружение, на котором будут запущены тесты
* `comment` - параметр позволяет выбрать комментарий из предложенных


#### Шаги для запуска автотестов через Jenkins

1. Открыть страницу <a target="_blank" href="https://github.com/Annatrg/litres">проекта</a>
2. В меню выбрать пункт `Build with Parameters`
3. Выбрать окружение в выпадающем списке
4. Выбрать комментарий
5. Нажать кнопку `Build`

После прохождения автотестов в Build History будет доступен отчет

![Jenkins build](./litres/image/Build.png)

----

### Allure отчет
#### Общие результаты

На странице с общими результатами мы можем увидеть общее количество тестов, сколько из них были успешными и сколько не успешными

![Allure_report_example](./litres/image/allure_report_result.png)

#### Отчет прохождения теста

В отчете для каждого кейса доступны 4 приложения. Среди них URL запроса, метод, тело запроса и куки 

![Allure_suites_test](./litres/image/allure_suites.png)


----

### Оповещения в Telegram

После выполнения автотестов, запущенных через Jenkins, также придёт уведомление в Telegram_bot об итогах тестирования

![allert_bot](./litres/image/allert_bot.png)

----
