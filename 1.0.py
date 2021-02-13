import pygame
import random

pygame.init()
Red = pygame.Color('Red')
Green = pygame.Color('Green')
Blue = pygame.Color('Blue')
Black = pygame.Color('Black')
White = pygame.Color('White')
# Запускаю игру и даю значение цветам
width, height = 800, 500
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption('Flappy Bird')
# Создаю размер окна и название игры
images = [pygame.image.load(str(i) + '.png') for i in range(1, 5)]
clock = pygame.time.Clock()
vector = pygame.math.Vector2
background = pygame.image.load('BackGround.png')
bg_w = background.get_width()
# Здесь я вызываю текстуру фона и птицы
probabilities = [[40, 320], [50, 310], [60, 300], [70, 290], [80, 280], [90, 270], [100, 260], [110, 250], [120, 240],
                 [130, 230], [140, 220], [150, 210], [160, 200], [170, 190], [180, 180],
                 [190, 170], [200, 160], [210, 150], [220, 140], [230, 130], [240, 120], [250, 110], [260, 100],
                 [270, 90], [280, 80], [290, 70], [300, 60], [310, 50], [320, 40]]


# ввожу все возможные положения прохода между трубами

class Bird(pygame.sprite.Sprite):

    def __init__(self, game):

        super().__init__()
        self.image = images[0]
        self.image = pygame.transform.scale(self.image, (100, 85))
        self.rect = self.image.get_rect()
        self.centre_otlet = vector(0, 0)
        self.rect.center = (width / 2, height / 2)
        self.gravity = vector(0, 0)
        self.pos = vector(self.rect.center)
        self.a_s = 0
        # Анимирую птицу

    def update(self):

        self.gravity = vector(0, 1)

        self.centre_otlet = vector(0, 0)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.gravity.y = -2
            # Устанавливаю силу взлёта
            if self.a_s + 1 < 28:
                self.a_s += 2
                self.image = images[self.a_s // 8]
                self.image = pygame.transform.scale(self.image, (100, 85))
                # Устанавливаю скорость анимации при удерживании пробела и размеры одного из кадров птицы

            else:
                self.a_s = 0

        else:
            self.image = images[0]
            self.image = pygame.transform.scale(self.image, (100, 85))
        self.centre_otlet += self.gravity
        self.pos += self.centre_otlet + 2 * self.gravity
        # Окончательно устанавливаю гравитацию
        if self.pos.y <= 0 + self.rect.width / 2:
            self.pos.y = 0 + self.rect.width / 2

        if self.pos.y >= height - self.rect.width / 2:
            self.pos.y = height - self.rect.width / 2
        self.rect.center = self.pos
        self.mask = pygame.mask.from_surface(self.image)
        # Устанавливаю размеры одного из кадров а также максимальную и минимальную высоту птицы


class PP2(pygame.sprite.Sprite):

    def __init__(self, x, h1):
        super().__init__()
        self.image = pygame.image.load('pipes2.png')
        self.image = pygame.transform.scale(self.image, (75, h1))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x + 180, 0

    def update(self):
        self.rect.x -= 2
        self.mask1 = pygame.mask.from_surface(self.image)
        # Настраиваю положение и размер верхних труб, а также расстояние между ними


class PP1(pygame.sprite.Sprite):

    def __init__(self, x, h2):
        super().__init__()

        self.image = pygame.image.load('pipes1.png')
        self.image = pygame.transform.scale(self.image, (75, h2))

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x + 180, height - self.rect.height

    def update(self):
        self.rect.x -= 2
        self.mask2 = pygame.mask.from_surface(self.image)
        # Настраиваю положение и размер нижних труб, а также расстояние между ними


class Game:

    def __init__(self):

        self.bgx = 0
        self.x = 800

        self.pp_1 = 180
        self.pp_2 = 180
        # Устанавливаю положение первых труб относительно птицы и размер отверстия между ними
        self.score = 0

        self.Game_Over = 0

        self.last = pygame.time.get_ticks()

    def PP_Gen(self):

        x = random.randint(620, 650)

        pp = random.choice(probabilities)

        pp_1 = pp[0]
        pp_2 = pp[1]

        self.pp2 = PP2(x, pp_1)
        self.pp2_1 = pygame.sprite.Group()
        self.pp2_1.add(self.pp2)

        self.all_sprites.add(self.pp2)

        self.pp1 = PP1(x, pp_2)
        self.pp1_1 = pygame.sprite.Group()
        self.pp1_1.add(self.pp1)

        self.all_sprites.add(self.pp1)
        # Настраиваю случайную генерацию труб

    def S_and_M(self):

        self.bird = Bird(self)

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.bird)

        self.pp2 = PP2(self.x, self.pp_1)
        self.pp2_1 = pygame.sprite.Group()
        self.pp2_1.add(self.pp2)

        self.all_sprites.add(self.pp2)

        self.pp1 = PP1(self.x, self.pp_2)
        self.pp1_1 = pygame.sprite.Group()
        self.pp1_1.add(self.pp1)

        self.all_sprites.add(self.pp1)

        self.score = 0

        self.Game_Over = 0
        # Даю значения функциям, а также активирую спрайты и анимации

    def msg(self, text, x, y, color, size):

        self.font = pygame.font.SysFont('Book Antiqua', size, bold=1)

        msgtxt = self.font.render(text, 1, color)
        msgrect = msgtxt.get_rect()
        msgrect.center = x / 2, y / 2

        screen.blit(msgtxt, (msgrect.center))
        # Выбираю шрифт и настраиваю центр текста

    def pause(self):

        wait = 1

        while wait:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()

                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        wait = 0

            self.msg("Paused", width - 100, height - 100, Blue, 40)
            # Осуществляю паузу
            pygame.display.flip()

    def GameOver(self):

        wait = 1

        self.Game_Over = 1

        while wait:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()

                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        wait = 0

            self.msg("Игра Окончена", width / 2, height - 350, Red, 55)

            self.msg("Нажмите 'Enter', чтобы продолжить мучать бедную птицу", width - 700, height + 250, Red, 24)
            # Осуществляю поражение и начало новой игры
            pygame.display.flip()

        self.S_and_M()

    def Score(self):

        self.msg("Score:" + str(self.score), width - 750, 50, Green, 30)
        # Указываю положение счёта и текст

    def update(self):

        self.all_sprites.update()

        Time = pygame.time.get_ticks()

        hit1 = pygame.sprite.spritecollide(self.bird, self.pp1_1, False, pygame.sprite.collide_mask)

        hit2 = pygame.sprite.spritecollide(self.bird, self.pp2_1, False, pygame.sprite.collide_mask)
        # Осуществляю столкновение с труб ами
        if hit1 or hit2:
            self.GameOver()

        bg_anim = self.bgx % bg_w + 5

        screen.blit(background, (bg_anim - bg_w + 3, 0))
        # Осуществляю движение заднего фона
        if bg_anim < width:
            screen.blit(background, (bg_anim, 0))

        self.bgx -= 2
        # Настраиваю скорость движения фона

        if self.pp1.rect.x < width / 2 and self.pp2.rect.x < width / 2:
            self.PP_Gen()

            self.score += 1

        if Time - self.last > 1500:

            self.last = Time

            self.score += 1

        else:

            self.score += 0
            # Настраиваю скорость увеличения счёта

    def draw(self):

        self.all_sprites.draw(screen)

        self.Score()
        # Вызываю спрайты и счёт, показывающиеся всегда

    def event(self):

        for event in pygame.event.get():

            clock.tick(60)
            # устанавливаю частоту кадров
            if event.type == pygame.QUIT:
                pygame.quit()

                quit()
                # Оптимизирую кнопку выхода
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:
                    self.pause()
                    # Оптимизирую паузу

    def run(self):

        while 1:
            self.event()

            self.update()

            self.draw()

            pygame.display.flip()


game = Game()

while game.run:
    game.S_and_M()
    game.run()
            # Активирую все элементы игры
