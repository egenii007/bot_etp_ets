#! /usr/bin/env python3
# -- coding: utf-8 --
from bs4 import BeautifulSoup
import requests
import time
import telebot
import datetime
from threading import Thread
from functools import wraps


import schedule

bot = telebot.TeleBot('1011013862:AAG6egwuWdxE34eaXmsNN39xMcz0EeiI4A4')


def get_html_torgi():
    r = requests.get("http://monit.etp-micex.ru/")
    return r.text


def get_status_torgi(html):
    main_data = []
    soup = BeautifulSoup(html, 'lxml')
    body = soup.find_all('div', class_='container')
    for i in body:
        main_data = i.find_all('h1')
    return main_data[2].text

# QQQ = get_status_torgi(get_html_torgi())
# print(QQQ)  # показывает активное количество торгов


# def select_torgi(x):  # зацикливание(мб так и надо, нужно ограничить до одного верного вхождения) #поменять местами
#     global a, r
#     a = 0
#     if x == "Активные торги : 0":
#         r = 'break'
#         print("BREAK")
#     elif x == "Активные торги : 0":  # a = 1
#         a += 1
#         r = "Торги на сегодня завершены"
#         print("ТОРГИ ЗАВЕРШЕНЫ")
#     return print(r)
# text = "Все торги на сегодня завершены. + \n + Предварительное начало торгов на " + time() + 1 + ":\n"


def end():  # зацикливание(мб так и надо, нужно ограничить до одного верного вхождения) #поменять местами
    global a, r
    y = get_status_torgi(get_html_torgi())
    while y != "Активные торги : 0":
        print("QWERTY")
        get_status_torgi(get_html_torgi())
        y = ""
        y += get_status_torgi(get_html_torgi())
    # return print(y)
    return bot.send_message(chat_id=545569185, text="Все торги на сегодня завершены.") and bot.send_message(chat_id=261171257, text="Все торги на сегодня завершены.")

# повторять каждый день с 10:00 весь код, а блок с выводом статуса в этот промежуток раз в минуту


# def replay():
#     now = datetime.datetime.now()
#     today13am = now.replace(hour=18, minute=20, second=0, microsecond=0)
#     bedtime = now.replace(hour=23, minute=50, second=0, microsecond=0)
#     if now > today13am:
#         select_torgi(QQQ)


# replay()
# ========================================================================================
def replay():
    now = datetime.datetime.now()
    print(now)
    today13am = now.replace(hour=00, minute=8, second=0, microsecond=0)
    bedtime = now.replace(hour=23, minute=50, second=0, microsecond=0)
    if today13am < now < bedtime:
        end()

# ========================================================================================


# def play():
#     if time == "23:45":
#         schedule.every().day.at("23:45").do(replay)
#         while True:
#             schedule.run_pending()


schedule.every().day.at("15:34").do(replay)
while True:
    schedule.run_pending()
    time.sleep(10)



# def mult_threading(func):
#     """Декоратор для запуска функции в отдельном потоке"""
#
#     @wraps(func)
#     def wrapper(*args_, **kwargs_):
#         import threading
#         func_thread = threading.Thread(target=func,
#                                        args=tuple(args_),      # ВСЕ ЭТО ДЛЯ QWERTY В РАЗДЕЛ def main_keyboard(message):
#                                        kwargs=kwargs_)
#         func_thread.start()
#         return func_thread
#
#     return wrapper
#
# @mult_threading
# def some_func():
#     schedule.every(2).minutes.do(replay)
#
#
# #  ==Проверяем работу==
# #  Стартуем нашу долгоиграющую функцию
#
# some_func()
# schedule.run_pending()
#


# def mainfun():
#
#     while True:  # если a = 1, то все прекратить
#         if select_torgi(QQQ) != 0:  # нет вызова данной функции
#             schedule.run_pending()
#             print("КУКУ")
#         elif select_torgi(QQQ) != 1:
#             print("Торги идут")
#             break
#         break
#
# mainfun()
# если в main выдало "Торги завершены", то стопать [schedule.Job (интервал, планировщик = нет) класс]


# select_torgi(QQQ)


# print(time.ctime())# запускать через while(рабочая неделя)
# print(time.monotonic())
# print(datetime.time(12,00,00))
# ПАРСИТЬ ВСЕ (В НАЧАЛЕ WHILE СТАВИТЬ) ПОКА НЕ НАСТУПИТ x ==  "Активные торги : 0"
# УЗНАВАТЬ СКОЛЬКО ТОРГОВ ОСТАЛОСЬ ПО СЕКЦИЯМ (ВЛОЖЕННЫЕ КНОПКИ)


# @bot.message_handler(content_types=['text'])
# def end_torgi(message):
#     def f():
#         schedule.every().day.at("00:10").do(replay)
#         while True:
#             schedule.run_pending()
#             time.sleep(10)
#     bot.send_message(message.chat.id, "Торги на сегодня завершены")