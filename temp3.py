from time import sleep

class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age

    def hash_password(self, password):
        return hash(password)

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:

    def __init__(self, users=[], videos=[], current_user=None):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and  user.password == self.hash_passwor(password):
                self.current_user = user
                return
        print('Неверный логин или пароль')

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = nickname

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for arg in args:
            if self.videos == []:
                self.videos.append(arg)
            else:
                # print(arg.title, 'it is ARG')
                for video in self.videos:
                    # print(video.title, 'it is video', video.title == arg.title)
                #     print(video.title,  arg.title, 'it are video.title and arg.title')
                    if video.title != arg.title:
                #         print(self.videos, 'it is videos befor')
                        self.videos.append(arg)
                #         print(self.videos, 'it is videos after' )

    def get_videos(self, word):
        list_titles = []
        for video in self.videos:
            # print(word.upper() in str(video.title).upper())
            if word.upper() in str(video.title).upper() and video.title not in list_titles:
                # print(word.upper(), str(video.title).upper())
                list_titles.append(video.title)
        return list_titles

    def watch_video(self, title):
        for video in self.videos:
            # print(video.adult_mode, video.title)

            if video.title == title and self.current_user != None:
                # print(self.current_user)
                for user in self.users:
                    # print(user.age)
                    if video.adult_mode == True and user.age >= 18 or video.adult_mode == False:
                        for i in range(video.duration):
                            video.time_now += 1
                            sleep(1)
                            print(video.time_now)
                        print('Конец видео')
                        video.time_now = 0
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
