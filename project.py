import random

import time

import pygame

from sup_func import *

FPS = 50
# размер экрана
size = width, height = 600, 400

pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption('Школа: нет пути домой')


def terminate():
    pygame.quit()
    sys.exit()


# начальный экран
def start_screen():
    load_music("sounds/mistika.mp3").play()
    intro_text = ["                        ШКОЛА: НЕТ ПУТИ ДОМОЙ", "",
                  "    Добро пожаловать в игру 'Школа: нет пути домой'!",
                  "    В игре Вам предстоит пройти путь из дома в школу, ",
                  "    но этот путь будет не так прост, как Вам кажется.",
                  "    На пути будет множество препятствий, которые ",
                  "    необходимо преодолеть. Удачи!",
                  "",
                  "",
                  "    УРОВЕНЬ:           ЛЕГКИЙ                   СРЕДНИЙ"]

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
    color1 = (255, 255, 255)
    color2 = (255, 255, 255)
    level_chosen = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            # работа с кнопками для выбора персонажа
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                if level1_rect.collidepoint(pygame.mouse.get_pos()):
                    color1 = (0, 255, 0)
                    color2 = (255, 255, 255)
                    print(pygame.mouse.get_pos())
                    level_chosen = 1
                elif level2_rect.collidepoint(pygame.mouse.get_pos()):
                    color1 = (255, 255, 255)
                    color2 = (0, 255, 0)
                    print(pygame.mouse.get_pos())
                    level_chosen = 2
                else:
                    print(pygame.mouse.get_pos())
                    if level_chosen != 0:
                        return level_chosen
                    else:
                        pass
                    # начинаем игру
        # тут рисуем женщин на выбор
        level1_rect = pygame.draw.rect(screen, color1, (170, 328, 30, 30), 40)
        level2_rect = pygame.draw.rect(screen, color2, (365, 328, 30, 30), 40)
        pygame.display.flip()
        clock.tick(FPS)


# экран выбора персонажа
def next_screen():
    pygame.mixer.music.stop()
    intro_text = ["                           ВЫБЕРИТЕ ПЕРСОНАЖА", "",
                  "             КСЮША              МАША                СТЕША"]

    fon = pygame.transform.scale(load_image('f2.jpg'), (size))
    screen.blit(fon, (0, 0))
    image_k = load_image('running K/00.png').convert_alpha()
    ksusha_image = pygame.transform.scale(image_k, (100, 135))
    screen.blit(ksusha_image, (75, 200))
    image_m = load_image('runningM/maria_0.png').convert_alpha()
    masha_image = pygame.transform.scale(image_m, (100, 135))
    screen.blit(masha_image, (245, 200))
    image_s = load_image('runningS/stesha_0.png').convert_alpha()
    stesha_image = pygame.transform.scale(image_s, (100, 135))
    screen.blit(stesha_image, (415, 200))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    pygame.display.flip()
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    color1 = (255, 255, 255)
    color2 = (255, 255, 255)
    color3 = (255, 255, 255)
    hero_chosen = 0
    while True:
        # тут рисуем женщин на выбор
        ksusha_rect = pygame.draw.rect(screen, color1, (115, 150, 30, 30), 40)
        maria_rect = pygame.draw.rect(screen, color2, (280, 150, 30, 30), 40)
        stesha_rect = pygame.draw.rect(screen, color3, (445, 150, 30, 30), 40)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                if ksusha_rect.collidepoint(pygame.mouse.get_pos()):
                    color1 = (0, 255, 0)
                    color2 = (255, 255, 255)
                    color3 = (255, 255, 255)
                    print(pygame.mouse.get_pos())
                    hero_chosen = 1
                elif maria_rect.collidepoint(pygame.mouse.get_pos()):
                    color1 = (255, 255, 255)
                    color2 = (255, 0, 0)
                    color3 = (255, 255, 255)
                    print(pygame.mouse.get_pos())
                    hero_chosen = 2
                elif stesha_rect.collidepoint(pygame.mouse.get_pos()):
                    color1 = (255, 255, 255)
                    color2 = (255, 255, 255)
                    color3 = (0, 0, 255)
                    print(pygame.mouse.get_pos())
                    hero_chosen = 3
                else:
                    print(pygame.mouse.get_pos())
                    if hero_chosen != 0:
                        return hero_chosen
                    else:
                        pass
                    # начинаем игру

        pygame.display.flip()
        clock.tick(FPS)


# класс с препятствиями
class Trap:
    def __init__(self, x, y, size: tuple, img):
        self.x = x
        self.y = y
        self.size = size
        self.img_rect = load_image(img)
        self.img_rect = pygame.transform.scale(self.img_rect, self.size)


# класс с монетами
class Money:
    def __init__(self, x, y, size: tuple, img):
        self.x = x
        self.y = y
        self.size = size
        self.img_rect = load_image(img)
        self.img_rect = pygame.transform.scale(self.img_rect, self.size)


# настройка переменных
x_fon = 0
fon_speed = 2
n_card = 0
dy = 0
y = 350
is_jump = False

font = pygame.font.Font(None, 30)

sound2 = load_music('sounds/bye.mp3')
sound4 = load_music('sounds/jump2.mp3')
sound5 = load_music('sounds/coin.mp3')

# Работаем с изображениями
fon_image = load_image("data/fon5.jpg")
fon_rect = pygame.transform.scale(fon_image, (1200, 400))

# начинается игра
start_screen()
hero_chosen = next_screen()
# загружаем нужного персонажа
hero_list = load_hero_images(hero_chosen)


# экран окончания
def game_over(is_rec):
    load_music("sounds/физика.mp3").play()
    fon = pygame.transform.scale(load_image('game_over.jpg'), (size))
    screen.blit(fon, (0, 0))
    if is_rec:
        print_text(0, 0, 'Новый рекорд', (255, 255, 255), screen)
    color1 = (255, 255, 255)
    start_chosen = 0
    while True:
        start_rect = pygame.draw.rect(screen, color1, (450, 270, 50, 30), 40)
        print_text(300, 310, 'Играть еще раз', (255, 255, 255), screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                if start_rect.collidepoint(pygame.mouse.get_pos()):
                    # color1 = (0, 255, 0)
                    print(pygame.mouse.get_pos())
                    start_chosen = 1
                    return next_screen()
                else:
                    print(pygame.mouse.get_pos())
                    if start_chosen != 0:
                        return start_chosen
                    else:
                        pass
                    # начинаем игру
        # тут рисуем женщин на выбор

        pygame.display.flip()
        clock.tick(FPS)
        pygame.display.update()


# функция генерирования препятствий-книг
def generate_trap(n, delta):
    x_b = 0
    trap_list = []
    for i in range(n):
        x_b += random.randint(300, 300 + delta) + 100
        trap_list.append(Trap(x_b, 340, (50, 50), './data/book.png'))
    return trap_list


# функция генерирования монет
def generate_money(n, trap_list):
    money_list = []
    for i in range(n):
        x_money = trap_list[i].x + 500
        y_money = random.randint(100, 330)
        money_list.append(Money(x_money, y_money, (50, 50), './data/coin.png'))

    return money_list


is_try_again = True
while is_try_again:
    print('Я продолжаюсь')
    is_game = True
    is_game_over = True
    is_jump = False

    hero_list = load_hero_images(hero_chosen)

    trap_list = generate_trap(4, 500)
    money_list = generate_money(3, trap_list)

    x_fon = 0
    fon_speed = 2
    n_card = 0
    dy = 0
    y = 350

    level_count = 1
    money_count = 0

    # прописываем прыжок
    while is_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not is_jump:
                    dy = -8
                    is_jump = True
                    sound4.play()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass

        x_fon -= fon_speed
        n_card += 1
        if len(trap_list) <= 0:
            trap_list = generate_trap(6, 300)
            money_list = generate_money(5, trap_list)
            fon_speed += 1
            level_count += 1

        if x_fon <= -600:
            x_fon = 0
        if n_card % 7 == 0:
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

        for trap in trap_list[::-1]:
            screen.blit(trap.img_rect, (trap.x, trap.y))
            trap.x -= fon_speed
            if trap.x < 0:
                trap_list.remove(trap)
            else:
                if trap.img_rect.get_rect(topleft=(trap.x, trap.y)).colliderect(
                        hero_list[n_card].get_rect(topleft=(50, y - 40))):
                    fon_speed = 0
                    sound2.play()
                    path_list = ['data/luzha.png' for _ in range(7)]
                    hero_list = [pygame.transform.scale(load_image(path), (60, 75)) for path in path_list]
                    is_game_over = False

        for money in money_list[::-1]:
            screen.blit(money.img_rect, (money.x, money.y))
            money.x -= fon_speed
            if money.x < 0:
                money_list.remove(money)
            else:
                if money.img_rect.get_rect(topleft=(money.x, money.y)).colliderect(
                        hero_list[n_card].get_rect(topleft=(50, y - 40))):
                    sound5.play()
                    money_list.remove(money)
                    money_count += 1

        print_text(30, 30, f'{level_count} уровень', (0, 0, 0), screen)
        print_text(width - 200, 30, f'Монеты: {money_count}', (0, 0, 0), screen)

        screen.blit(hero_list[n_card], (50, y - 40))

        pygame.display.flip()
        clock.tick(FPS)

        if not is_game_over:
            pygame.time.delay(2000)
            is_rec = check_record('./record.txt', level_count)
            if is_rec:
                save_record_to_txt('./record.txt', level_count, money_count)
            is_game = False

    is_try_again = game_over(is_rec)
