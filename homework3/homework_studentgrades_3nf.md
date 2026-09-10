# Домашняя работа: Нормализация базы данных StudentGrades

## Раздел 1. Основы проектирования баз данных

### Часть 1. Теоретический анализ

#### 1. Первичный ключ исходной таблицы

В исходной таблице до нормализации для однозначного определения результата можно использовать составной ключ:

`(student_id, subject_id, exam_date)`

Он однозначно определяет результат конкретного студента по конкретному предмету в определённую дату.

Однако после нормализации в таблице `StudentGrades` используется отдельный идентификатор `id`, который является первичным ключом. Поля `student_id`, `subject_id` и `teacher_id` становятся внешними ключами (`FOREIGN KEY`).

Почему отдельные поля не подходят в качестве первичного ключа:

- `student_id` не подходит, потому что один студент может иметь несколько результатов;
- `subject_id` не подходит, потому что один предмет могут сдавать разные студенты;
- `teacher_id` не подходит, потому что один преподаватель может принимать несколько тестов.

#### 2. Функциональные зависимости

Основные функциональные зависимости исходной таблицы:

```text
student_id → student_name
student_id → group_id
group_id → group_name
teacher_id → teacher_name
subject_id → subject_name
(student_id, subject_id, exam_date) → grade
```

После нормализации эти зависимости распределяются между отдельными таблицами.

#### 3. Транзитивные зависимости

В исходной таблице присутствует транзитивная зависимость:

```text
student_id → group_id → group_name
```

То есть `student_id` определяет `group_id`, а `group_id` определяет `group_name`.

Также:

```text
subject_id → subject_name
teacher_id → teacher_name
```

Поэтому названия группы, предмета и преподавателя следует вынести в отдельные таблицы.

#### 4. Нормальная форма исходной таблицы

Исходная таблица находится в **1НФ**.

Все значения являются атомарными, то есть в каждой ячейке хранится одно значение.

Таблица не соответствует 2НФ, поскольку при использовании составного ключа `(student_id, subject_id, exam_date)` некоторые атрибуты зависят только от части ключа:

```text
student_id → student_name
subject_id → subject_name
```

Также присутствуют транзитивные зависимости, поэтому исходная таблица не соответствует 3НФ.

---

# Часть 2. Практическая нормализация до 3НФ

## Итоговый список таблиц

После нормализации получились следующие таблицы:

1. `Groups` — группы студентов.
2. `Students` — студенты.
3. `Teachers` — преподаватели.
4. `Subjects` — учебные предметы.
5. `StudentGrades` — результаты тестирования.

---

## ER-схема

```text
┌──────────────────┐
│      Groups      │
├──────────────────┤
│ PK id            │
│ group_name       │
└────────┬─────────┘
         │ 1
         │
         │ N
┌────────▼─────────┐
│     Students     │
├──────────────────┤
│ PK id            │
│ student_name     │
│ FK group_id      │
└────────┬─────────┘
         │ 1
         │
         │ N
         │
┌────────▼────────────────────┐
│       StudentGrades         │
├─────────────────────────────┤
│ PK id                       │
│ FK student_id               │
│ FK subject_id               │
│ FK teacher_id               │
│ exam_date                   │
│ grade                       │
└─────────┬───────────┬───────┘
          │ N         │ N
          │           │
          │ 1         │ 1
┌─────────▼───────┐ ┌─▼──────────────┐
│    Subjects     │ │    Teachers    │
├─────────────────┤ ├────────────────┤
│ PK id            │ │ PK id          │
│ subject_name    │ │ teacher_name   │
└─────────────────┘ └────────────────┘
```

### Связи между таблицами

```text
Groups 1 ─── N Students
Students 1 ─── N StudentGrades
Subjects 1 ─── N StudentGrades
Teachers 1 ─── N StudentGrades
```

---

---

# Пример заполнения таблиц

## Groups

| id | group_name |
|---:|---|
| 1 | Группа А |
| 2 | Группа Б |

## Students

| id | student_name | group_id |
|---:|---|---:|
| 1 | Петров П. | 1 |
| 2 | Иванов И. | 1 |
| 3 | Сидоров С. | 2 |
| 4 | Петров П. | 1 |
| 5 | Кузнецов К. | 2 |

## Teachers

| id | teacher_name |
|---:|---|
| 1 | Петрова М. |
| 2 | Смирнов А. |
| 3 | Козлова Е. |

## Subjects

| id | subject_name |
|---:|---|
| 1 | Математика |
| 2 | Физика |
| 3 | Информатика |

## StudentGrades

| id | student_id | subject_id | teacher_id | exam_date | grade |
|---:|---:|---:|---:|---|---:|
| 1 | 1 | 1 | 1 | 2026-01-15 | 4 |
| 2 | 2 | 2 | 2 | 2026-01-20 | 3 |
| 3 | 3 | 1 | 1 | 2026-01-18 | 5 |
| 4 | 4 | 3 | 3 | 2026-01-25 | 5 |
| 5 | 5 | 2 | 2 | 2026-01-22 | 4 |

---

# Типы данных и параметры

| Таблица | Поле | Тип | Параметры |
|---|---|---|---|
| Groups | id | INT | PRIMARY KEY |
| Groups | group_name | VARCHAR(50) | NOT NULL, UNIQUE |
| Students | id | INT | PRIMARY KEY |
| Students | student_name | VARCHAR(100) | NOT NULL |
| Students | group_id | INT | NOT NULL, FOREIGN KEY |
| Teachers | id | INT | PRIMARY KEY |
| Teachers | teacher_name | VARCHAR(100) | NOT NULL |
| Subjects | id | INT | PRIMARY KEY |
| Subjects | subject_name | VARCHAR(50) | NOT NULL, UNIQUE |
| StudentGrades | id | INT | PRIMARY KEY |
| StudentGrades | student_id | INT | NOT NULL, FOREIGN KEY |
| StudentGrades | subject_id | INT | NOT NULL, FOREIGN KEY |
| StudentGrades | teacher_id | INT | NOT NULL, FOREIGN KEY |
| StudentGrades | exam_date | DATE | NOT NULL |
| StudentGrades | grade | INT | NOT NULL |

---

# Вывод

После нормализации исходная таблица была разделена на 5 связанных таблиц: `Groups`, `Students`, `Teachers`, `Subjects` и `StudentGrades`.

В каждой таблице используется отдельное поле `id` в качестве первичного ключа. Внешние ключи связывают таблицы между собой. Это позволяет избежать дублирования данных и привести структуру базы данных к третьей нормальной форме (3НФ).
