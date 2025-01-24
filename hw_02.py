for i in range(3,21):
    # print(i)
    for k in range(1, i):
        # print(k, "it'is k")
        for l in range(1, k):
            # print(l, 'it is l')
            if i % (k+l) == 0:
                # print(i, 'it is i', k, '+', l)
                print(i, '-', l, k)



# def get_matrix(n, m, value):
#     matrix =[]
#     for i in range(n):
#         matrix.append([])
#         for _ in range(1, m):
#             matrix[i].append(value)
#     return matrix
#
# result1 = get_matrix(2, 2, 10)
# result2 = get_matrix(3, 5, 42)
# result3 = get_matrix(4, 2, 13)
# print(result1)
# print(result2)
# print(result3)
#
# import time
#
# t1_start = time.time()
# numbers = []
# for n in range (1, 10000):
#     numbers.append(n)
# primes = set()
# not_primes = set()
# numbers = set(numbers)
# num_iter = 0
#
#
# for i in numbers:
#     is_prime = True
#     if i == 1:
#         not_primes.add(i)
#     for n in range(2, i):
#         num_iter += 1
#         if i % n == 0:
#             not_primes.add(i)
#             is_prime = False
#             break # with break, num_iter = 5 775 222, time = 0,7sec, without break, num_iter = 49 975 003, time = 6,3sec
#     if is_prime == True and i != 1:
#         primes.add(i)
#
# # primes = numbers - not_primes
#
#
# primes = list(primes)
# not_primes = list(not_primes)
#
# t1_finish = time.time()
# print(t1_finish-t1_start)
#
# print(sorted(primes))
# print(len(primes))
# print(not_primes)
# print(len(not_primes))
# print(num_iter)
#
#
# import time
# # то что было в первом решении:
#
# my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
#
# number = int()
# number_of_index = 0
# len_my_list = len(my_list)
#
# t1_start = time.time()
# while number >= 0:
#     for i in range(10000):
#         i ** 1555
#     number = my_list[number_of_index]
#     if number > 0:
#         print(number)
#     number_of_index = number_of_index + 1
#
#     if number_of_index == len_my_list:
#         break
# t1_finish = time.time()
# print(t1_finish-t1_start)
#
# # то что было во втором решении:
# my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
#
# number = int()
# number_of_index = 0
# len_my_list = len(my_list)
#
# while number >= 0:
#
#     number = my_list[number_of_index]
#     if number > 0: # and number != 0:
#         print(number)
#     number_of_index = number_of_index + 1
#
#     if number_of_index == len_my_list:
#         break
#
#
# # module 2.3
# my_list =  [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# index = 0
# t2_start = time.time()
# while index < len(my_list):
#     if my_list[index] < 0:
#         break
#     elif my_list[index] > 0:
#         for i in range(10000):
#             i**1555
#         print(my_list[index])
#     index += 1
# t2_finish = time.time()
# print(t2_finish-t2_start)
#
#
# # module 2.2
# def func(a):
#     if str(a)[0]==str(a)[1] and str(a)[0]==str(a)[2]:
#         print(3)
#     elif  (str(a)[0]==str(a)[1] and str(a)[0]!=str(a)[2] or str(a)[0]!=str(a)[1] and str(a)[0]==str(a)[2]
#            or str(a)[0]!=str(a)[1] and str(a)[1]==str(a)[2]):
#         print(2)
#     else:
#         print(0)
#
#
# func(545)