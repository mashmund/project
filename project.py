import os
import random
import sys

import pygame

pygame.init()
size = width, height = 600, 400
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


def load_image(name):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


FPS = 50


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["                        ШКОЛА: НЕТ ПУТИ ДОМОЙ", "",
                  "    Добро пожаловать в игру 'Школа: нет пути домой'!",
                  "    В игре Вам предстоит пройти путь из дома в школу, ",
                  "    но этот путь будет не так прост, как Вам кажется.",
                  "    На пути будет множество препятствий, которые ",
                  "    необходимо преодолеть. Удачи!"]

    fon = pygame.transform.scale(load_image('project_start_fon.jpg'), (size))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


start_screen()
