# TodoSqlAlchemy
Приклад використання SqlAlchemy для реалізації ORM - об'єктно-реляційної проекції.
Як приклад використовується додаток "Список справ (To do)", який складається з двох зв'язаних таблиць:

```
TODO_LIST - списки справ
CREATE TABLE todo_list
(
    id integer NOT NULL DEFAULT nextval('todo_list_id_seq'::regclass),
    name character varying(20) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT todo_list_pkey PRIMARY KEY (id)
)

TODO_ITEM - елементи списків справ
CREATE TABLE todo_item
(
    id integer NOT NULL DEFAULT nextval('todo_item_id_seq'::regclass),
    txt character varying(50) COLLATE pg_catalog."default" NOT NULL,
    done boolean NOT NULL,
    list_id integer NOT NULL,
    CONSTRAINT todo_item_pkey PRIMARY KEY (id),
    CONSTRAINT todo_fk FOREIGN KEY (list_id)
        REFERENCES public.todo_list (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)
```

### Встановлення

У командному рядку (терміналі) слід увести наступну команду для завантаження коду репозиторія:
 
```git clone https://github.com/Aroxed/TodoSqlAlchemy.git```

Встановити необхідні бібліотеки:
```pip install -r requirements.txt```

### Запуск програми:

```python main.py```

## Опис файлів:

- ```main.py``` призначений для запуску програми і тестування розроблених класів
- ```database.py``` призначений для інкапсуляції об'єктів SqlAlchemy і реалізації деяких методів доступу до бази 
- ```model.py``` призначений для опису класів TodoList і TodoItem, які власне і є проекцією на відповідні таблиці бази даних 

## Результат роботи програми:
```
(todoSQLAlchemy) > python main.py
All list with items:
{'Work for today': 'Wash the car, Write a letter', 'Work for tomorrow': 'Clean the room, Go swimming'}

All list with done items:
{'Work for today': 'Write a letter', 'Work for tomorrow': 'Go swimming'}
```