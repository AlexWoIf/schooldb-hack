# ВЗЛОМ ШКОЛЬНОЙ БАЗЫ ДАННЫХ

## Описание

[Урок 3 Знакомство с Django: ORM «Взламываем электронный дневник»](https://dvmn.org/modules/django-orm/lesson/correcting-grades/)

Данный код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org)

В файле `scripts.py` содержатся скрипты позволяюще проводить манипуляции с учебной базой данных имитирующей базу данных некой школы.

Важное замечание: *база данных, а также код сайта школы в данный репозиторий не включены!*

## Предварительные требования

Скрипты работают только на основе [сайта электронных дневников](https://github.com/devmanorg/e-diary/tree/master).

Для использования скриптов нужно клонировать репозиторий урока и скачать и подключить файл базы данных.

Так же необходимо выполнить все инструкции, которые содержатся в репозитории и тексте урока.

Это обязательно для продолжения работы.

## Запуск

- Скопируйте файл 'scripts.py' в папку проекта, где содержится файл 'manage.py'
- Запустите Django Shell командой 'python manage.py shell'
- В терминале роимпортируйте библиотеку скриптов 'import scripts'
- Вы готовы к работе!

## Описание функционала и примеры использования

- Получаем объект "ученик" по его имени:

```child = scripts.get_schoolkid_entity("Фролов Иван")```

- Исправляем все плохие оценки (2 и 3) на отличные (5)

```scripts.fix_marks(schoolkid=child)```

- Удаляем все не замечания ученика

```scripts.remove_chastisements(schoolkid=child)```

- Добавляем похвалу к последнему проведенному уроку нужного предмета

```create_commendation(name="Фролов Иван", subject="Музыка")```