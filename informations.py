#! /usr/bin/env python3
# -- coding: utf-8 --
import telebot

from telebot import TeleBot

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



# def get_time_container():
#     r44 = 'https://www.etp-ets.ru/procedure/catalog/?&conditionalHoldingDateTime-from=' + time() + '&conditionalHoldingDateTime-to=' + time() + '&procedureStatusId[]=65&procedureStatusId[]=$
#     r223 = 'https://www.etp-ets.ru/223/catalog/procedure?&tradeStartDateTime-from=' + time() + '&tradeStartDateTime-to=' + time() + '&lotStatusId[]=31&lotStatusId[]=33&'
#     def torgi(html):
#         soup = BeautifulSoup(html, 'lxml')
#         body = soup.find_all('div', class_='input-group pull-right mte-grid-pageLimiter')
#         for day in body:
#             day1 = day.find('span', class_='input-group-addon')
#             for q in day1:
#                 w = q.find("span")
#         return q
#     return 'По 44: ' + torgi(get_html(r44)) + '\n' + 'По 223: ' + torgi(get_html(r223))





