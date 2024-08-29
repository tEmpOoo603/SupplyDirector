- Склонируйте репозиторий и установите зависимости "pip install -r requirements.txt"-
- Создайте в postgresql пользователя с именем "root" и паролем "root", а также выдайте все разрешение
- Создайте базу данных postgresql с именем "file_system" и владельцем - root
- По умолчанию сервер postgresql запускается на локалхосте на порте 5432
- Примените все миграции "python manage.py migrate"
- Создайте суперпользователя для доступа к админке python manage.py createsuperuser
- запустить сервер "python manage.py runserver"
- В админке можно так же работать со всеми Ивентами и Изменениями ивентов 127.0.0.1:8000/admin/

# API реализован с префиксом /api/
Список команд и возможностей:
- POST  add/
Добавить событие со следующими параметрами в виде json:
name [str] — название события
start_at [int, unix timestamp в секундах (UTC)] — время и дата начала события
period [int | None] — как часто должно повторяться событие (например, при period = 7 событие будет повторяться каждую неделю)
Возвращается json с полем id — уникальный id первого созданного события

- POST  remove/{id}/{year}/{month}/{day}/
Удалить конкретное событие по его id (как и в гугл-календаре: нужно удалить только ТЕКУЩЕЕ событие, а не все события из цепочки повторения)

- POST  remove-next/{id}/{year}/{month}/{day}/
Удалить конкретное событие по его id и все последующие по цепочке

- POST  update/{id}/{year}/{month}/{day}/
Изменить название конкретного события по его id (как и в гугл-календаре: нужно изменить только ТЕКУЩЕЕ событие, а не все события из цепочки повторения). Параметры в виде json:
name [str] — новое название события

- GET  events/{year}/{month}/{day}/
Получить в ответ список событий в указанный день (в списке указывать name и id события)
