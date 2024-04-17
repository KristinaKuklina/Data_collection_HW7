# Задание
1. Выберите веб-сайт, который содержит информацию, представляющую интерес для извлечения данных. 
Это может быть новостной сайт, платформа для электронной коммерции или любой другой сайт, 
который позволяет осуществлять скрейпинг (убедитесь в соблюдении условий обслуживания сайта).
2. Используя Selenium, напишите сценарий для автоматизации процесса перехода на нужную страницу сайта.
3. Определите элементы HTML, содержащие информацию, которую вы хотите извлечь (например, заголовки статей, 
названия продуктов, цены и т.д.).
4. Используйте BeautifulSoup для парсинга содержимого HTML и извлечения нужной информации из идентифицированных элементов.
5. Обработайте любые ошибки или исключения, которые могут возникнуть в процессе скрейпинга.
6. Протестируйте свой скрипт на различных сценариях, чтобы убедиться, что он точно извлекает нужные данные.
7. Предоставьте ваш Python-скрипт вместе с кратким отчетом (не более 1 страницы), который включает следующее: 
    - URL сайта. Укажите URL сайта, который вы выбрали для анализа. 
    - Описание. Предоставьте краткое описание информации, которую вы хотели извлечь из сайта. 
    - Подход. Объясните подход, который вы использовали для навигации по сайту, определения соответствующих элементов
  и извлечения нужных данных. 
    - Трудности. Опишите все проблемы и препятствия, с которыми вы столкнулись в ходе реализации проекта, 
и как вы их преодолели. 
    - Результаты. Включите образец извлеченных данных в выбранном вами структурированном формате (например, CSV или JSON). 
Примечание: Обязательно соблюдайте условия обслуживания сайта и избегайте чрезмерного скрейпинга, который может нарушить 
нормальную работу сайта.

# Отчет 

1. URL сайта (сайт онлайн-магазина кофе): "https://shop.tastycoffee.ru/?ysclid=lv1fnhl3fe445267367"
2. Информация, извлекаемая из сайта:
    - название;
    - описание кофе;
    - цена за 250 г;
    - цена за 1 кг.
    Кофе должен соответствовать заданным фильтрам: степени обжарки, помолу
3. Подход. 
  Для навигации по сайту производился поиск селекторов нужных элементов с последующим кликом. Для перехода
  к окнам и кнопкам для настроек фильтров, а также подгрузке всех результатов, отвечающих фильтрам, использовался
  язык запросов XPath. 
  Перед первым поиском селектора на сайте использовался метод wait, ожидающий, пока элемент не станет доступен
  для взаимодействия.
  Для ожидания применения фильтров и загрузки всех результатов использовалась функция, отслеживающая текущий URL страницы.
  После загрузки всех результатов с помощью библиотеки BeautifulSoup производился поиск
  карточек и нужной информации из них.
4. Трудности.
  - на этапе поиска карточек найденные карточки не соответствовали указанным фильтрам. Это вызвано тем, 
    что поиск осуществлялся без ожидания загрузки новых результатов после указания фильтров. Проблема 
    решена с использованием функции, приостанавливающей код до тех пор, пока текущий URL не станет отличным
    от того, который был до вызова click.
5. Результаты работы программы в прикрепленном файле "tasty_coffee.csv".