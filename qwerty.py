#! /usr/bin/env python3
# -- coding: utf-8 --
import datetime
from datetime import timedelta, datetime
import lxml
import requests
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth
import telebot

A = ['CAACAgIAAxkBAAICI14y80NZWdrZzfffM_cr9FUbKTZqAAJQCQACeVziCfUAATaxAAEx80gYBA',
     'CAACAgIAAxkBAAICJF4y86_hQEZnbvjmkxoFMEtoKKbkAAJKCQACeVziCWyGrjj1_IOoGAQ',
     'CAACAgIAAxkBAAICJV4y89CARSb7yvgU06tTC_gFUqZXAAJJCQACeVziCT6IJiuxU355GAQ',
     'CAACAgIAAxkBAAICJl4y8-mDnO-7jA0PmzthpQ2qw_23AAJfCQACeVziCZCAjXmZR2L6GAQ',
     'CAACAgIAAxkBAAICJ14y8_2sa4iVFNFX8V6QPMqAi33KAAJmCQACeVziCZ8KivlhthhEGAQ',
     'CAACAgIAAxkBAAICKF4y9BPzIqITIRSAbjZHgJH0lQgwAAJWCQACeVziCdI_3yy7G-XkGAQ',
     'CAACAgIAAxkBAAICNF4y9Fvjr21tLam0_3IbDbgKQ8spAAJVCQACeVziCa9amrleRn9xGAQ'
     ]
bot = telebot.TeleBot('1011013862:AAG6egwuWdxE34eaXmsNN39xMcz0EeiI4A4')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Отчет из nagios', 'Торги на данный момент', 'Запланированно на завтра')

def tomorrow():
    tomorrow_date = (datetime.now() + timedelta(days=1)).strftime("%d.%m.%Y")
    return tomorrow_date

def now():
    now = datetime.now()
    site = now.strftime("%d.%m.%Y") .__str__()
    return site

def get_html(url):  # аутентификация и получение странички Nagios
    r = requests.get(url, auth=HTTPBasicAuth("monitoring", "monitoring"))  # авторизация
    return r.text

def get_data(html):  # парсинг nagios
    Q = []
    V = 1
    soup = BeautifulSoup(html, 'lxml')  # lxml интерпретатор html кода
    body = soup.find_all('body', class_="status")
    for metrics in body:
        m = metrics.find_all('table', class_="status", width="100%", border="0")
        for page in m:
            ls = page.find_all("td", class_="statusBGCRITICAL")
            for qwerty in ls:
                open = qwerty.find_all("td", class_="statusBGCRITICAL", valign="center", align="left")
                for x in open:
                    y = x.find_all("a")
                    for q in y:
                        z = q.get("href")
                        p = V.__str__() + ') http://nagios-m1.etp-micex.ru/nagios/cgi-bin/' + z
                        V += 1
                        Q.append(p)

    XXX = "\n\nCRITICAL\n\n".join(Q[:-1])
    return XXX


def get_time_container(time):
    r44 = 'https://www.etp-ets.ru/procedure/catalog/?&conditionalHoldingDateTime-from=' + time + '&conditionalHoldingDateTime-to=' + time + '&procedureStatusId[]=65&procedureStatusId[]=72&fullSearch=0&'
    r223 = 'https://www.etp-ets.ru/223/catalog/procedure?&tradeStartDateTime-from=' + time + '&tradeStartDateTime-to=' + time + '&lotStatusId[]=31&lotStatusId[]=33&'
    def torgi(html):
        soup = BeautifulSoup(html, 'lxml')
        body = soup.find_all('div', class_='input-group pull-right mte-grid-pageLimiter')
        for day in body:
            day1 = day.find('span', class_='input-group-addon')
            for q in day1:
                w = q.find("span")
                q1 = [int(s) for s in q.split() if s.isdigit()]
                q2 = "".join([str(i) for i in q1])
                return q2
    return 'По 44 всего: ' + torgi(get_html(r44)).__str__() + '\n' + 'По 223 всего: ' + torgi(get_html(r223)).__str__()+'\n'+ 'По имущественным: '

def property_bidding():  # имущественные торги
    r1 = 'https://www.etp-torgi.ru/market/?action=search&search_type=all&search_record_on_page=10&search_string=&procedure_stage=auction&price_from=&price_to=&currency=0&search_by_date_type=&$'
    r2 = 'https://www.etp-torgi.ru/market/?action=search&search_type=all&search_record_on_page=10&search_string=&procedure_stage=wait_auction_begin&price_from=&price_to=&currency=0&search_by_$'

    def get_time_container(html):
        global w
        soup = BeautifulSoup(html, 'lxml')
        body = soup.find_all('div', class_='row_page')  # если body = [], то return 0 иначе...

        if body != []:
            for x in body:
                y = x.find("div", class_='count_lots').text
            q1 = [int(s) for s in y.split() if s.isdigit()]
            q2 = "".join([str(i) for i in q1])
            return int(q2)
        else:
            y = 0
            return y

    return (get_time_container(get_html(r1))) + (get_time_container(get_html(r2)))
#    return 'Идут торги: ' + (get_time_container(get_html(r1))) + '\n' + 'Ожидаются:' + (get_time_container(get_html(r2)))

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'привет, ты написал мне /start', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'отчет из nagios':
        bot.send_message(message.from_user.id, get_data(get_html("http://nagios-m1.etp-micex.ru/nagios/cgi-bin/status.cgi?host=all&servicestatustypes=16&sorttype=1&sortoption=6")))
    elif message.text.lower() == 'торги на данный момент':
        bot.send_message(message.from_user.id, get_time_container(now())+property_bidding().__str__())
    elif message.text.lower() == 'запланированно на завтра':
        bot.send_message(message.from_user.id, get_time_container(tomorrow())+property_bidding().__str__())
    else:
        bot.send_message(message.from_user.id, "я тебя не понимаю. Напиши /help.")

bot.polling(none_stop=True, interval=1)


