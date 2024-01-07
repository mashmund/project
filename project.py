import os
import random
import sys
import pygame

FPS = 50
size = width, height = 600, 400

pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


def load_image(name):
    fullname = os.path.join('', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


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


def next_screen():
    intro_text = ["                           ВЫБЕРИТЕ ПЕРСОНАЖА", "",]

    fon = pygame.transform.scale(load_image('f2.jpg'), (size))
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
    color1 = (0, 0, 0)
    color2 = (0, 0, 0)
    color3 = (0, 0, 0)
    hero_chosen = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                if ksusha_rect.collidepoint(pygame.mouse.get_pos()):
                    color1 = (0, 255, 0)
                    color2 = (0, 0, 0)
                    color3 = (0, 0, 0)
                    print(pygame.mouse.get_pos())
                    hero_chosen = 1
                elif maria_rect.collidepoint(pygame.mouse.get_pos()):
                    color1 = (0, 0, 0)
                    color2 = (255, 0, 0)
                    color3 = (0, 0, 0)
                    print(pygame.mouse.get_pos())
                    hero_chosen = 2
                elif stesha_rect.collidepoint(pygame.mouse.get_pos()):
                    color1 = (0, 0, 0)
                    color2 = (0, 0, 0)
                    color3 = (0, 0, 255)
                    print(pygame.mouse.get_pos())
                    hero_chosen = 3
                else:
                    print(pygame.mouse.get_pos())
                    return hero_chosen
                    # начинаем игру
        # тут рисуем женщин на выбор
        ksusha_rect = pygame.draw.rect(screen, color1, (30, 30, 30, 30), 40)
        maria_rect = pygame.draw.rect(screen, color2, (70, 30, 30, 30), 40)
        stesha_rect = pygame.draw.rect(screen, color3, (110, 30, 30, 30), 40)
        pygame.display.flip()
        clock.tick(FPS)



class Hero:
    def __init__(self):
        # x, y, rect
        pass


class Trap:
    pass


# настройка переменных
x_fon = 0
fon_speed = 2
n_card = 0
dy = 0
y = 350
is_jump = False
trap_list = [Trap(), Trap()]

# Работаем с изображениями
fon_image = load_image("fon2.png")
fon_rect = pygame.transform.scale(fon_image, (1200, 400))

# начинается игра
start_screen()
hero_chosen = next_screen()

# загружаем нужного персонажа
if hero_chosen == 1:
    path_list = ['бежит/0.png', 'бежит/1.png', 'бежит/2.png', 'бежит/3.png']
    hero_list = [pygame.transform.scale(load_image(path), (60, 60)) for path in path_list]
if hero_chosen == 2:
    path_list = ['бежит/0.png', 'бежит/1.png', 'бежит/2.png', 'бежит/3.png']
    hero_list = [pygame.transform.scale(load_image(path), (60, 60)) for path in path_list]
if hero_chosen == 3:
    path_list = ['бежит/0.png', 'бежит/1.png', 'бежит/2.png', 'бежит/3.png']
    hero_list = [pygame.transform.scale(load_image(path), (60, 60)) for path in path_list]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jump:
                dy = -5
                is_jump = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass

    x_fon -= fon_speed
    n_card += 1
    if x_fon <= -600:
        x_fon = 0
    if n_card % 4 == 0:
        n_card = 0
    # гравитация
    y += dy
    dy += 0.2

    if y >= 350:
        y = 350
        dy = 0
        is_jump = False

    # отрисовка всех штук на экране
    screen.blit(fon_rect, (x_fon, 0))
    ground = pygame.draw.rect(screen, (100, 100, 100), (0, 340, 600, 400), 40)

    for trap in trap_list:
        pass

    screen.blit(hero_list[n_card], (50, y - 40))

    pygame.display.flip()
    clock.tick(FPS)
