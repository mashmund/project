
import random


import time
from sup_func import *

FPS = 50
size = width, height = 600, 400

pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


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
        # тут рисуем женщин на выбор
        ksusha_rect = pygame.draw.rect(screen, color1, (115, 150, 30, 30), 40)
        maria_rect = pygame.draw.rect(screen, color2, (280, 150, 30, 30), 40)
        stesha_rect = pygame.draw.rect(screen, color3, (445, 150, 30, 30), 40)
        pygame.display.flip()
        clock.tick(FPS)


class Hero:
    def __init__(self):
        # x, y, rect
        pass


class Trap:
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
trap_list = [Trap(300, 320, (35, 35), './data/book.png'),
             Trap(900, 320, (35, 35), './data/book.png')]

# Работаем с изображениями
fon_image = load_image("fon2.png")
fon_rect = pygame.transform.scale(fon_image, (1200, 400))



# начинается игра
start_screen()
hero_chosen = next_screen()
# загружаем нужного персонажа
hero_list = load_hero_images(hero_chosen)
def game_over():
    fon = pygame.transform.scale(load_image('game_over.jpg'), (size))
    screen.blit(fon, (0, 0))
    while True:
        pygame.display.flip()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                return True

x_b = 0
trap_list = []
for i in range(5):
    x_b += random.randint(300, 800) + 150
    trap_list.append(Trap(x_b, 360, (30, 30), './data/book.png'))


is_try_again = True
while is_try_again:
    print('Я продолжаюсь')
    is_game = True
    is_game_over = True
    count_luzha = 0
    hero_list = load_hero_images(hero_chosen)
    x_fon = 0
    fon_speed = 2
    n_card = 0
    dy = 0
    y = 350
    is_jump = False
    while is_game:
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

        for trap in trap_list:
            screen.blit(trap.img_rect, (trap.x, trap.y))
            trap.x -= fon_speed
            if trap.img_rect.get_rect(topleft=(trap.x, trap.y)).colliderect(
                    hero_list[n_card].get_rect(topleft=(50, y - 40))):
                fon_speed = 0
                path_list = ['data/luzha.png' for _ in range(7)]
                hero_list = [pygame.transform.scale(load_image(path), (60, 75)) for path in path_list]
                is_game_over = False


        screen.blit(hero_list[n_card], (50, y - 40))

        pygame.display.flip()
        clock.tick(FPS)

        if not is_game_over:
            pygame.time.delay(2000)
            is_game = False

    is_try_again = game_over()