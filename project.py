import os

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


# функция выхода
def terminate():
    pygame.quit()
    sys.exit()


# начальный экран
def start_screen():
    # создание тхт файла, если его еще нет
    if not os.path.exists('./record.txt'):
        save_record_to_txt('./record.txt', 0, 0)
    # запись в тхт файл начального уровня
    with open('./record.txt', 'r+') as f:
        if not f.readline():
            f.write('0;0')
    # загрузка и воспроизведение начальной музыки
    load_music('sounds/mistika.mp3').play()
    # текст введения в игру
    intro_text = ['                        ШКОЛА: НЕТ ПУТИ ДОМОЙ', '',
                  '    Добро пожаловать в игру "Школа: нет пути домой"!',
                  '    В игре Вам предстоит пройти путь из дома в школу, ',
                  '    но этот путь будет не так прост, как Вам кажется.',
                  '    На пути будет множество препятствий, которые ',
                  '    необходимо преодолеть. Удачи!',
                  '',
                  'ВЫБЕРИТЕ УРОВЕНЬ:         ЛЕГКИЙ                 СРЕДНИЙ',
                  '',
                  '               Нажмите пробел для выбора персонажа']

    # фон
    fon = pygame.transform.scale(load_image('project_start_fon.jpg'), (size))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50

    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color("white"))
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
        # создание кнопок для выбора уровня
        level1_rect = pygame.draw.rect(screen, color1, (250, 300, 30, 30), 40)
        level2_rect = pygame.draw.rect(screen, color2, (435, 300, 30, 30), 40)
        # просматриваем варианты событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            # работа с кнопками для выбора персонажа
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                if level1_rect.collidepoint(pygame.mouse.get_pos()):
                    # если выбрали 1 уровень
                    color1 = (255, 0, 0)
                    color2 = (255, 255, 255)
                    level_chosen = 1

                elif level2_rect.collidepoint(pygame.mouse.get_pos()):
                    # если выбрали 3 уровень
                    color1 = (255, 255, 255)
                    color2 = (255, 0, 0)
                    level_chosen = 2

                else:
                    # если ничего не выбрали
                    if level_chosen != 0 and (event.type == pygame.KEYDOWN or event.type == pygame.K_SPACE):
                        return level_chosen
                    else:
                        pass

        pygame.display.flip()
        clock.tick(FPS)


# экран выбора персонажа
def next_screen():
    # остановка сузыки с прошлого экрана
    pygame.mixer.music.stop()
    # текст выбора персонажа
    intro_text = ['                           ВЫБЕРИТЕ ПЕРСОНАЖА', '',
                  '             КСЮША              МАША                СТЕША'
                  '',
                  '',
                  '',
                  '',
                  '',
                  '',
                  '',
                  '',
                  '                  Нажмите пробел, чтобы начать игру']

    # фон
    fon = pygame.transform.scale(load_image('f2.jpg'), (size))
    screen.blit(fon, (0, 0))

    # работа с фото ксюши
    image_k = load_image('running K/00.png').convert_alpha()
    ksusha_image = pygame.transform.scale(image_k, (100, 135))
    screen.blit(ksusha_image, (75, 200))

    # работа с фото маши
    image_m = load_image('runningM/maria_0.png').convert_alpha()
    masha_image = pygame.transform.scale(image_m, (100, 135))
    screen.blit(masha_image, (245, 200))

    # работа с фото стеши
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
        # создание "кнопок" для выбора персонажа
        ksusha_rect = pygame.draw.rect(screen, color1, (115, 150, 30, 30), 40)
        maria_rect = pygame.draw.rect(screen, color2, (280, 150, 30, 30), 40)
        stesha_rect = pygame.draw.rect(screen, color3, (445, 150, 30, 30), 40)

        # просматриваем варианты событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                if ksusha_rect.collidepoint(pygame.mouse.get_pos()):
                    # если нажали на "ксюшу"
                    color1 = (0, 255, 0)
                    color2 = (255, 255, 255)
                    color3 = (255, 255, 255)
                    hero_chosen = 1

                elif maria_rect.collidepoint(pygame.mouse.get_pos()):
                    # если нажали на "ксюшу"
                    color1 = (255, 255, 255)
                    color2 = (255, 0, 0)
                    color3 = (255, 255, 255)
                    hero_chosen = 2

                elif stesha_rect.collidepoint(pygame.mouse.get_pos()):
                    # если нажали на "ксюшу"
                    color1 = (255, 255, 255)
                    color2 = (255, 255, 255)
                    color3 = (0, 0, 255)
                    hero_chosen = 3
                else:
                    # если ничего не выбрали
                    if hero_chosen != 0 and (event.type == pygame.KEYDOWN or event.type == pygame.K_SPACE):
                        return hero_chosen
                    else:
                        pass

        # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


# экран окончания
def game_over(is_rec):
    # загрузка и воспроизведение музыки
    load_music("sounds/физика.mp3").play()
    # фон
    fon = pygame.transform.scale(load_image('game_over.jpg'), (size))
    screen.blit(fon, (0, 0))
    if is_rec:
        print_text(0, 0, 'Новый рекорд', (255, 255, 255), screen)
    color1 = (255, 255, 255)
    start_chosen = 0
    while True:
        # "кнопка" для повторной игры
        start_rect = pygame.draw.rect(screen, color1, (450, 270, 50, 30), 40)
        print_text(300, 310, 'Играть еще раз', (255, 255, 255), screen)
        # просматриваем варианты событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                if start_rect.collidepoint(pygame.mouse.get_pos()):
                    # color1 = (255, 0, 0)
                    # start_chosen = 1
                    return next_screen()
                else:
                    return 0

        pygame.display.flip()
        clock.tick(FPS)
        pygame.display.update()


# функция генерирования препятствий-книг
def generate_trap(n, delta):
    x_b = 0
    trap_list = []
    for i in range(n):
        x_b += random.randint(300, 300 + delta) + 100
        trap_list.append(Trap(x_b, 340, fon_speed, (50, 50), './data/book.png'))

    # возвращает список препятствий
    return trap_list


# функция генерирования монет
def generate_money(n, trap_list):
    money_list = []
    for i in range(n):
        x_money = trap_list[i].rect.x + 500
        y_money = random.randint(120, 330)
        money_list.append(Money(x_money, y_money, fon_speed, (50, 50), './data/coin.png'))

    # возвращает список монет
    return money_list


# создание собственного события
IS_GAMEOVER_CHANGED = pygame.USEREVENT + 2

# создание собственного события
IS_MONEY_CHANGED = pygame.USEREVENT + 3


# класс с героем
class Hero(pygame.sprite.Sprite):
    def __init__(self, x, y, hero_chosen):
        super().__init__(all_sprites)
        self.n_cadr = 0
        self.imgs = load_hero_images(hero_chosen)
        self.image = self.imgs[self.n_cadr]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dy = 0
        self.is_jump = False
        self.n_cadr = 0

    def update(self):
        # прыжок
        if self.is_jump:
            self.rect.y += self.dy
            self.dy += 0.2
        # отмена прыжка
        if self.rect.y >= 310:
            self.rect.y = 310
            self.is_jump = False
            self.dy = 0
        self.n_cadr += 1
        # анимация
        self.image = self.imgs[self.n_cadr % 7]
        self.mask = pygame.mask.from_surface(self.image)


# класс с препятствиями
class Trap(pygame.sprite.Sprite):
    def __init__(self, x, y, fon_speed, size: tuple, img):
        super().__init__(trap_sprites)
        self.image = load_image(img)
        self.size = size
        self.image = pygame.transform.scale(self.image, self.size)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.fon_speed = fon_speed

    def update(self):
        self.rect.x -= self.fon_speed
        # взаимодействие персонажей в случае их столновения
        if pygame.sprite.collide_mask(self, hero):
            # превращение персонажа в лужу
            path_list = ['data/luzha.png' for _ in range(7)]
            hero.imgs = [pygame.transform.scale(load_image(path), (60, 75)) for path in path_list]
            # остановка движения
            self.fon_speed = 0
            # воспроизведение звука
            sound2.play()
            # переход с персональному событию
            pygame.event.post(pygame.event.Event(IS_GAMEOVER_CHANGED))

        # исчезновение препятствий по мере продвижения их по дороге
        if self.rect.x <= 0:
            self.kill()

    def new_level(self):
        # увеличение скорости фона
        self.fon_speed += 1


# класс монет
class Money(pygame.sprite.Sprite):
    def __init__(self, x, y, fon_speed, size: tuple, img):
        super().__init__(all_sprites)
        self.image = load_image(img)
        self.size = size
        self.image = pygame.transform.scale(self.image, self.size)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.fon_speed = fon_speed

    def update(self):
        self.rect.x -= self.fon_speed
        # взаимодействие персонажей в случае их столновения
        if pygame.sprite.collide_mask(self, hero):
            # воспроизведение звука
            sound5.play()
            # переход с персональному событию
            pygame.event.post(pygame.event.Event(IS_MONEY_CHANGED))
            # исчезновение монеты
            self.kill()
        # исчезновение препятствий по мере продвижения их по дороге
        if self.rect.x <= 0:
            self.kill()

    def new_level(self):
        # увеличение скорости фона
        self.fon_speed += 1


# настройка переменных
x_fon = 0
fon_speed = 2
n_card = 0

is_jump = False

font = pygame.font.Font(None, 30)

# загружаем музыку
sound2 = load_music('sounds/bye.mp3')
sound4 = load_music('sounds/jump2.mp3')
sound5 = load_music('sounds/coin.mp3')

# Работаем с изображениями
fon_image = load_image("data/fon100.jpg")
fon_rect = pygame.transform.scale(fon_image, (1200, 400))

# начинается игра
level_chosen = start_screen()
hero_chosen = next_screen()

# загружаем нужного персонажа
hero_list = load_hero_images(hero_chosen)


while hero_chosen:
    is_game = True
    is_game_over = False
    is_jump = False
    fon_speed = 2

    # создадим группу, содержащую все спрайты
    all_sprites = pygame.sprite.Group()
    # создадим группу, содержащую все спрайты препятствияч
    trap_sprites = pygame.sprite.Group()
    # персонаж
    hero = Hero(50, 310, hero_chosen)

    # список с препятствиями
    trap_list = generate_trap(4, 500)
    # список с монетами
    money_list = generate_money(3, trap_list)

    x_fon = 0
    y = 350

    # если 1 уровень
    if level_chosen == 1:
        fon_speed = 2
        level_count = 1

    # если 2 уровень
    elif level_chosen == 2:
        fon_speed = 4
        level_count = 3
    money_count = 0

    # прописываем прыжок
    while is_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            # событие прижка
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not hero.is_jump:
                    hero.dy = -8
                    # прыжок
                    hero.is_jump = True
                    # воспроизведение звука
                    sound4.play()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass

            # персональное событие остановки игры
            elif event.type == IS_GAMEOVER_CHANGED:
                # остановка фона
                fon_speed = 0
                is_game_over = True

            # персональное событие счета игры
            elif event.type == IS_MONEY_CHANGED:
                # увеличение количества монет
                money_count += 1

        x_fon -= fon_speed

        # если список пустой
        if len(trap_sprites) <= 0:
            # обновления спика препятствий
            trap_list = generate_trap(6, 300)
            # обновления спика монет
            money_list = generate_money(5, trap_list)
            # увеличение скорости
            fon_speed += 1
            # повышение уровня
            level_count += 1

        # обновление фона
        if x_fon <= -600:
            # перехол на начало
            x_fon = 0

        # отрисовка всех штук на экране
        screen.blit(fon_rect, (x_fon, 0))
        # отрисовка земли
        ground = pygame.draw.rect(screen, (100, 100, 100), (0, 340, 600, 400), 40)

        # обновление препятствий
        trap_sprites.update()
        # обновление монет и персонажа
        all_sprites.update()

        # отрисовка монет, персонажа
        all_sprites.draw(screen)

        # отрисовка препятствий
        trap_sprites.draw(screen)

        # вывод текста об текущем уровне
        print_text(30, 30, f'{level_count} уровень', (0, 0, 0), screen)

        # вывод текста о текущем количестве монет
        print_text(width - 200, 30, f'Монеты: {money_count}', (0, 0, 0), screen)

        pygame.display.flip()
        clock.tick(FPS)

        if is_game_over:
            pygame.time.delay(2000)
            # проверка на наличие рекорда
            is_rec = check_record('./record.txt', level_count)

            # если есть
            if is_rec:
                # запись в тхт файл о новом рекорде
                save_record_to_txt('./record.txt', level_count, money_count)
            is_game = False

    hero_chosen = game_over(is_rec)