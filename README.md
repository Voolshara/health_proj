# Stroke Recover Service

на данный момент демо сайта находится на http://45.91.8.150:4600/
баланс на 18.08 хватает ещё на неделю работы

## Документация к проекту

### сервис разработан на VUE + Python (Flask)

связка с помощью fetch

# FrontEnd VUE3/CLI

## Фунционал

- Главная старица (будет новая)
- Форма
- 2 формы по инсульту
- 8 заданий
- админ панель (общая страница + отдельная страница)
- 2 бота
- начало лк (реализованы сессии)

## Используемые технологии

- [Vue Router](https://router.vuejs.org/) роутинг
- [Elements Plus](https://element-plus.org/en-US/) дизайн элементов
- [Анимации](https://www.npmjs.com/package/vue3-animate-onscroll) на базе animate.css
- Авторизация реализована с помозью VueX

## Роутизация

> файл app.vue содержит тэг `<router-view />`  
> здесь рэндэрится каждый роут

файл router.js содержит всю информацию о роутах
все роуты хранятся в папке `/src/routes`

большинство роутов имеют компаненты, импортируемые из `/src/components/`

### Авторизация

реализация авторизации практически полностью скатана от [сюда](https://www.bezkoder.com/vue-3-authentication-jwt/)
если при переходе на ссылки ниже в куках нет токена, то пользоваиеля перекинет на `/login`

> `/start` > `/form1` > `/form2` > `/task1` > `/task2` > `/task3` > `/task4` > `/task5` > `/task6` > `/task7` > `/task8`

файлы связанные с этим функционалом:

- `/src/services/*` (3 файла \*.js)
- `/src/store/*`

## Боты

Боты разработаны целиком на стороне фронта (внутри тэга `<script>` файла Vue)
`TODO` : вынести логику на бэк
файлы ботов

- `/src/components/bot.vue` (зелённая кнопка)
- `/src/components/hard_bot.vue` (жёлтая конпка)

## Запуск фронта

необходимо: npm, vue/cli

Install the dependencies and devDependencies and start the server.

для тестирования

```sh
cd frontend
npm i
npm run serve
```

билд проекта

```sh
cd frontend
npm i
npm run build
```

# Backend Python Flask

В проекте используется [poetry](https://python-poetry.org/docs/)
версия Python 3.10 и выше

перед стартом нужно утсановить poetry а после

```sh
cd backend
poetry shell
poetry install
```

БД высупает mysql (в проекте используется алхимия, так что не большой разницы какую БД юзать)

Далее подготовить переменные среды

| Переменная      | Значение        |
| --------------- | --------------- |
| MySQL_NAME      | Юзер БД         |
| MySQL_PASSWORD  | Пароль юзера    |
| MySQL_HOST      | хост БД         |
| MySQL_PORT      | порт БД         |
| MySQL_DB_NAME_2 | имя базы данных |

проверить подключение к БД можно с помощью

```sh
cd backend
poetry shell
set_db
```

если код завершился без ошибки, то в пустую БД добивились все Таблицы

## Запуск Сервера

после всех предилущих шагов запускаем

```sh
cd backend
poetry shell
run_server
```

#### Общая информация по бэку

вся логика работа с БД вынесена в `/backend/src/db/db.py`
классы, определённые в этом файле вызываются в `/backend/src/main.py`

### Cood Luck
