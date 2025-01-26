from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self, users=[('max', 'as', 12), ], videos=[], current_user=None):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self, nickname, password):
        for i in self.users:
            if i[0] == nickname:
                if password == i[1]:
                    self.current_user = nickname

                    print(f'identification successful for {nickname}')
                else:
                    print(f'Incorrect password for {nickname}')

    def log_out(self):
        self.current_user = None

    def register(self, nickname, password, age):
        flag_nickname = False
        for n in self.users:
            if n[0] == nickname:
                print(f'Пользователь {nickname} уже существует')
                break
            else:
                flag_nickname = True
        if flag_nickname == True:
            self.current_user = nickname
            self.users.append((f'{nickname}', f'{password}', f'{age}'))

    def add(self, *videos):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, word):
        list_title = []
        for v in self.videos:
            # print(v.title, 'IT IS v!!!!!!!!!!')
            if word.upper() in v.title.upper():
                list_title.append(v.title)
        return list_title

    def watch_video(self, title):
        for v in self.videos:
            if title == v.title:
                if ur.current_user != None:
                    if v.adult_mode == True:
                        for u in self.users:
                            if u[0] == ur.current_user:
                                if int(u[2]) >= 18:
                                    for i in range(v.time_now, v.duration + 1):
                                        sleep(0.2)
                                        print(i, end='')
                                    print('\nКонец видео')
                                else:
                                    print(f'{u[0]} {u[2]} Вам нет 18 лет, пожалуйста покиньте страницу')
                    else:
                        print('Войдите в аккаунт, чтобы смотреть видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
