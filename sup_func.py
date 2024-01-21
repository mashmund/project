# загружаем нужного персонажа
import os
import pygame
import sys


# функция загрузки изображения
def load_image(name):
    fullname = os.path.join('', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


# функция загрузки звука
def load_music(name):
    fullname = name
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл со звуком '{fullname}' не найден")
        sys.exit()
    return pygame.mixer.Sound(fullname)


# функция загрузки изображения персонажа
def load_hero_images(hero_chosen):
    if hero_chosen == 1:
        path_list = ['running K/00.png', 'running K/00.png', 'running K/ksusha_2.png', 'running K/ksusha_2.png',
                     'running K/ksusha_2.png', 'running K/00.png', 'running K/00.png']
        hero_list = [pygame.transform.scale(load_image(path), (60, 75)) for path in path_list]
    if hero_chosen == 2:
        path_list = ['runningM/maria_0.png', 'runningM/maria_0.png', 'runningM/maria_2.png', 'runningM/maria_2.png',
                     'runningM/maria_2.png', 'runningM/maria_0.png', 'runningM/maria_0.png']
        hero_list = [pygame.transform.scale(load_image(path), (60, 75)) for path in path_list]
    if hero_chosen == 3:
        path_list = ['runningS/stesha_0.png', 'runningS/stesha_0.png', 'runningS/stesha_2.png', 'runningS/stesha_2.png',
                     'runningS/stesha_2.png', 'runningS/stesha_0.png', 'runningS/stesha_0.png']
        hero_list = [pygame.transform.scale(load_image(path), (60, 75)) for path in path_list]
    return hero_list


# функция вывод текста
def print_text(x, y, text, color, screen):
    font = pygame.font.Font(None, 40)
    font_rend = font.render(text,1, color)
    screen.blit(font_rend,(x,y))


# функция сохранения результата в тхт
def save_record_to_txt(path, level, money):
    with open(path, 'w') as f:
        f.write(f'{level};{money}')


# функция записи результата в тхт файл
def check_record(path, level):
    with open(path, 'r') as f:
        rec_level, rec_money = map(int, f.readline().split(';'))
        if level > rec_level:
            return True
        else:
            return False
