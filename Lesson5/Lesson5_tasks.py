# 1) Создать декоратор, который будет запускать функцию в отдельном
# потоке. Декоратор должен принимать следующие аргументы:
# название потока, является ли поток демоном.
# 2) Создать функцию, которая будет скачивать файл из интернета по
# ссылке, повесить на неё декоратор, который будет запускать целевую
# функцию каждый раз в отдельном потоке. Создать список из 10
# ссылок, по которым будет происходить скачивание. Каждый поток
# должен сигнализировать, о том, что, он начал работу и по какой
# ссылке он работает, так же должен сообщать когда скачивание
# закончится.
# 3) Написать свой контекстный менеджер для работы с файлами.
# 4) Дополнение к предыдущей работе с соц. Сетью. Все хранение
# данных пользователей реализовать на основе модуля shelve.
#t4 = Thread(target=io_bound, args=(4, 5), name='Самый долгий поросенок', daemon=True)
# Task 1


def thread_decorator(th_name, is_daemon=False):

    def actual_decorator(func):
        from threading import Thread

        def wrapper(*args, **kwargs):
            t = Thread(target=func, args=(*args,), kwargs={**kwargs}, name=th_name, daemon=is_daemon)
            result = t.start()
            print(f'Название потока: {t.getName()}\n')
            return result

        return wrapper

    return actual_decorator


import time

@thread_decorator('Test')
def io_bound(id_, sec):
    print(f'{id_} Уснула\n')
    time.sleep(sec)
    print(f'{id_} Проснулась\n')

parms = [(1, 2), (2, 3), (3, 3), (4, 2), (5, 4), (6, 3), (7, 1)]

for i in parms:
    io_bound(*i)

#===============================================================Task 2


def thread_decorator(th_name, is_daemon=False):

    def actual_decorator(func):
        from threading import Thread
        import time

        def wrapper(*url_file):
            t = Thread(target=func, args=(url_file,), name=th_name, daemon=is_daemon)
            print(f'Скачивание началось по ссылке: {url_file}')
            time.sleep(3)
            result = t.start()
            return result

        return wrapper

    return actual_decorator

@thread_decorator('thread_download')
def download_file(url_file):
    import requests
    req = requests.get(url_file, stream=False)
    req.raise_for_status()
    with open(url_file[url_file.rfind('/') + 1:], 'wb') as fd:
        for chunk in req.iter_content(chunk_size=0):
            fd.write(chunk)
            print(f"Скачивание файла {url_file[url_file.rfind('/') + 1:]} завершено")

urls = ['https://www.davno.ru/assets/images/cards/big/birthday-1061.jpg',
        'https://oboi.ws/wallpapers/13_9016_oboi_kosmos_1280x800.jpg',
        'https://oboi.ws/wallpapers/22_7156_oboi_bliz_jupitera_640x960.jpg',
        'https://srcc.oboi.ws/wallpapers/big_9692_oboi_kosmicheskij_vihr.jpg',
        'https://srcc.oboi.ws/wallpapers/big_8621_oboi_magnitnye_buri.jpg',
        'https://srca.oboi.ws/wallpapers/big_4314_oboi_glubiny_neobjatnogo_kosmosa.jpg',
        'https://srcc.oboi.ws/wallpapers/big_5507_oboi_jevakuacija_s_gibnushhej_planety.jpg',
        'https://srca.oboi.ws/wallpapers/big_9723_oboi_illjustracii_kosmosa.jpg',
        'https://srca.oboi.ws/wallpapers/big_5598_oboi_planeta_na_fone_zvezdy.jpg',
        'https://srca.oboi.ws/wallpapers/big_5607_oboi_unknown.jpg']


for i in urls:
    download_file(i)
#============================================= Task 3


class MyOpen:

    def __init__(self, file_name, method):
        self.file_name = file_name
        self.method = method

    def __enter__(self):
        self.file = open(self.file_name, self.method)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


h = 'Hello world'
with MyOpen('test.txt', 'w') as f:
    f.write(h)

# ============================================ Task 4