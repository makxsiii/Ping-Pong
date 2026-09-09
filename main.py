from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Ping-Pong')
background = transform.scale(image.load('Без имени1234.png'), (500,500))

class GameSprite(sprite.Sprite):
    def __init__(self, pl_image, x, y, pl_speed, sx, sy):
        super().__init__()
        self.image = transform.scale(image.load(pl_image), (sx, sy))
        self.speed = pl_speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    @staticmethod
    def draw_text(size, txt, rgb, pos):
        game_font = font.Font(None, size)
        rendered_txt = game_font.render(txt, True, rgb)
        window.blit(rendered_txt, pos)
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 395:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 395:
            self.rect.y += self.speed        

racket1 = Player('Без имени1.png', 5, 200, 1, 20, 100)
racket2 = Player('Без имени1.png', 675, 200, 1, 20, 100)

clock = time.Clock()
FPS = 60

game = True
while game:
    window.blit(background, (0, 0))
    racket1.update_l()
    racket2.update_r()
    racket1.show()
    racket2.show()  

    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)