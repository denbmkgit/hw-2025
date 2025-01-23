def send_email(message, recipient, sender="university.help@gmail.com"):
    if '@' not in recipient:
        print(f"1 recipient {recipient} Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif '@' not in sender:
        print(f"2 sender {sender} Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif sender[-4:] != '.com':# or sender[-3:] != '.ru' or sender[-4:] != '.net':
        print(f"3 Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif recipient[-4:] == '.com' or recipient[-3:] == '.ru' or recipient[-4:] == '.net':
        print(f"4 Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif sender == recipient:
        print('5 Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'6 Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    if sender != 'university.help@gmail.com':
        print(f'7 НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.ru')
# send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
# send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
# send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')







# # home_work_3_1
# calls = 0
# def count_calls():
#     global calls
#     calls += 1
#     return calls
#
# def string_info(string):
#     count_calls()
#     cortege = (len(string), string.upper(), string.lower())
#     return cortege
#
#
# def is_contains(string, list_to_search):
#     count_calls()
#     for i in list_to_search:
#         if string.upper() in str(i).upper():
#             return True
#     else:
#        return False
#
# print(string_info('Capybara'))
# print(string_info('Armageddon'))
# print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
# print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
# print(calls)