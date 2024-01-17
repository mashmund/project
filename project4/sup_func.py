# загружаем нужного персонажа
import os
import pygame
import sys


def load_image(name):
    fullname = os.path.join('', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image

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