# home_work_3_hard
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]


sum_all = 0

def calculate_structure_sum(d_t):
    global sum_all
    for i in d_t:
        print(i)
        if type(i)==str:
            sum_all += len(i)
        if type(i) == int:
            sum_all += i
        # if type(i) == dict:
        #     for key, value in i.items():
        #         if type(key) == str:
        #             sum_all += len(i)
        #         if type(key) == int:
        #             sum_all += i
        #         if type(value) == str:
        #             sum_all += len(i)
        #         if type(value) == int:
        #             sum_all += i
        # else:
        #     calculate_structure_sum(i)
    return sum_all





# print(sum_all)
result = calculate_structure_sum(data_structure)
print(result)


# # home_work_3_5
# def get_multiplied_digits(number=int):
#     str_number = str(number)
#     first = int(str_number[0])
#     # print(first, 'first')
#     # print(str_number, 'str_number')
#     # sum_n = sum(int(num) for num in str(str_number))
#
#     if len(str_number) == 2 and int(str_number[-1]) == 0:
#         return first
#     # elif int(str_number) == 0:
#     #     return first
#     elif len(str_number) > 1:
#         return first * get_multiplied_digits(int(str_number[1:]))
#     else:
#         return first
#
#
# result = get_multiplied_digits(40203)
# print(result)
# result2 = get_multiplied_digits(402030)
# print(result2)










# # home_work_3_4
# def single_root_words(root_word, *other_words):
#     same_word = []
#     if len(same_word) < 3:
#         for word in other_words:
#             if root_word.upper() in word.upper() or word.upper() in root_word.upper():
#                 same_word.append(word)
#     return same_word
#
# result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
# result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
# print(result1)
# print(result2)

# # home_work_3_3
# def print_params(a = 1, b = 'строка', c = True):
#     print(a, b, c)
#
# print_params()
# print_params(b = 25)
# print_params(c = [1,2,3])
#
# values_list_2 = [54.32, 'Строка' ]
# print_params(*values_list_2, 42)
# print()
# print()
# values_list = [3, 4.0, 'str']
# values_dict = {'a':3, 'b': 'str_2', 'c': 5.0}
# values_dict_2 = {'a':3, 'c': 'str_2', 'b': 5.0}
# print_params(*values_list)
# print()
# print(values_dict)
# print()
# print_params(**values_dict)
# print_params(**values_dict_2)



# # home_work_3_2
# def send_email(message, recipient, sender="university.help@gmail.com"):
#     a = 0
#     if '@' in recipient and '@' not in sender:
#         a += 1
#     if  '.com' in sender[-4:] or '.ru' in sender[-3:] or '.net' in sender[-4:]:
#         a += 1
#     if  '.com' in recipient[-4:] or '.ru' in recipient[-3:] or '.net' in recipient[-4:]:
#         a += 1
#     if a < 2:
#         print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
#         return
#     if recipient == sender:
#         print('Нельзя отправить письмо самому себе!')
#         return
#     if sender == 'university.help@gmail.com':
#         print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
#     if sender != 'university.help@gmail.com':
#         print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
#
# send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.ru')
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