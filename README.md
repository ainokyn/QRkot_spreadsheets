# Финальный проект спринта: приложение QRkot_spreadseets

## Описание проекта
Данный проект представляет сопой приложение по сбору пожертвований на котиков.
Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых,
на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели,
связанные с поддержкой кошачьей популяции.
Проект состоит из проектов, пожертвований, пользователей.
В проект добавлена новая возможность: формировать отчет в гугл-таблице. В таблице должны быть закрытые проекты,
отсортированные по скорости сбора средств — от тех, что закрылись быстрее всего, до тех, что долго собирали нужную сумму.

**Проекты:**

В Фонде QRKot может быть открыто несколько целевых проектов. У каждого проекта есть название, описание и сумма,
которую планируется собрать. После того, как нужная сумма собрана — проект закрывается.
Пожертвования в проекты поступают по принципу First In, First Out: все пожертвования идут в проект, открытый раньше
других; когда этот проект набирает необходимую сумму и закрывается — пожертвования начинают поступать в следующий проект.

**Пожертвования:**

Каждый пользователь может сделать пожертвование и сопроводить его комментарием. Пожертвования не целевые: они вносятся в фонд,
а не в конкретный проект. Каждое полученное пожертвование автоматически добавляется в первый открытый проект, который ещё не набрал
нужную сумму. Если пожертвование больше нужной суммы или же в Фонде нет открытых проектов — оставшиеся деньги ждут открытия
следующего проекта. При создании нового проекта все неинвестированные пожертвования автоматически вкладываются в новый проект.

**Пользователи:**

Целевые проекты создаются администраторами сайта.
Любой пользователь может видеть список всех проектов, включая требуемые и уже внесенные суммы.
Это касается всех проектов — и открытых, и закрытых.
Зарегистрированные пользователи могут отправлять пожертвования и просматривать список своих пожертвований.
Суперпользователь может:
создавать проекты,
удалять проекты, в которые не было внесено средств,
изменять название и описание существующего проекта, устанавливать для него новую требуемую сумму
(но не меньше уже внесённой).
Никто не может менять через API размер внесённых средств, удалять или модифицировать закрытые проекты,
изменять даты создания и закрытия проектов.

**Процесс инвестирования:**

Сразу после создания нового проекта или пожертвования должен запускаться процесс «инвестирования»
(увеличение invested_amount как в пожертвованиях, так и в проектах, установка значений fully_invested и close_date, при необходимости).
Если создан новый проект, а в базе были «свободные» (не распределённые по проектам) суммы пожертвований — они автоматически
должны инвестироваться в новый проект, и в ответе API эти суммы должны быть учтены. То же касается и создания пожертвований:
если в момент пожертвования есть открытые проекты, эти пожертвования должны автоматически зачислиться на их счета.
Функции, отвечающие за инвестирование, должны вызываться непосредственно из API-функций, отвечающих за создание пожертвований и проектов. 

**Отчеты**

Таблицы с отчетами содержат в себе следующие элемены:
- Шапку с датой формировния отчета
- Названия проектов
- Количество дней, которое потребовалось для закрытия проекта
- Описания проектов


**Процесс формирования отчетов**

Для получения отчета надо сделать GET запрос на эндпоинт:'http://127.0.0.1:8000/google/'
Чтобы интегрировать новую возможность в проект, были добавлены:
- настройки для работы c Google API;
- метод получения данных, сгруппированных в соответствии с задачей;
- функции управления сервисам Google API;
- эндпоинт для использования новой возможности.
В результате приложение достает из базы данных нужную информацию и сохранять её в виде отчёта в гугл-таблице.


## Стек технологий

- Python 3
- FastAPI
- FastAPI Users
- SQLAlchemy(asyncio)
- Alembic
- Google Sheets API
- Google Drive API
- Aiogoogle