# **Приложение: "Помощник ученика"**

Приложение проверяет расписание уроков в электронном дневнике (на сайте [http://school.nso.ru](school.nso.ru)) на завтрашний день через заданный промежуток времени, отслеживает изменения в этом расписании, отслеживает появление или удаление домашнего задания по какому-либо предмету.  Приложение оповещает пользователя об изменениях через email, текстовое сообщение или WhatApp. 

## Возможно необходимые модули
 1. Архитектура : Backend / Frontend  ([подробнее...](https://blog.skillfactory.ru/chem-frontend-otlichaetsya-ot-backenda-obyasnyaem-na-memah/))
 2. Формат хранение рассписания (включая домашние задания) в приложении. ([подробнее...](https://ru.stackoverflow.com/questions/1182125/%D0%A7%D1%82%D0%BE-%D0%BB%D1%83%D1%87%D1%88%D0%B5-%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D1%8C-json-sql-%D0%B8%D0%BB%D0%B8-%D1%87%D1%82%D0%BE-%D1%82%D0%BE-%D0%B4%D1%80%D1%83%D0%B3%D0%BE%D0%B5))  
 3. Модуль авторизации ([подробнее...](https://www.digitalocean.com/community/tutorials/how-to-get-started-with-the-requests-library-in-python-ru))
 4. Модуль парсинга ( [подробнее... ](https://timeweb.com/ru/community/articles/chto-takoe-parser))
 5. ....

Для каждого модуля можно создать "issue" и "branch" для осуждения и разработки
<!DOCTYPE html>
<html>
    <head>
      <title>
        Programm
      </title>
    </head>
    <style>
        h1{
            color:rgb(10,7,0)
        }
    </style>
    <body>
        <h1>Расписание изменилось</h1>
        <p>Предмет *литература* был удалён из расписания. Предметы *информатика*, *химия* были добавлены. 
        </p>
        <p>Следующая проверка состоится в **:**</p>
        <h1>Список домашнего задания изменился</h1>#Список обновлённого расписания сравнивается со списком из предыдущей проверки. Задание по удалённому предмету не указывается по умолчанию.  Также по умолчанию указываются задания по добавленным предметам.
        <p>Д/З по информатике: *****
               Д/З по химии: *****
               новое Д/З по русскому языку: *****
               новое Д/З по ОБЖ: *****
        <p1>
        <p>Следующая проверка расписания состоится в **:**<p1>#Расписание и список заданий проверяются отдельно, но в одно и то же время
        <h1>Хорошего дня!</h1>#Вывод всех данных осуществляется через условный оператор(это уже часть Backend). Для всех возможных условий и итогов проверки мне нужно будет создать отдельные тексты в Frontend по аналогичному принципу.                         
    </body>
</html>
