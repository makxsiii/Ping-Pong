from pygame import *
font.init()

window = display.set_mode((700, 500))
display.set_caption('Ping-Pong')
background = transform.scale(image.load('Без имени1234.png'), (700, 500))

WIN1 = font.Font(None, 70).render('PLAYER_1 WINNER!', True, (255, 255, 255))
WIN2 = font.Font(None, 70).render('PLAYER_2 WINNER!!', True, (255, 255, 255))

score1 = 0
score2 = 0

finish = False

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

racket1 = Player('Без имени12.png', 5, 200, 5, 20, 100)
racket2 = Player('Без имени12.png', 675, 200, 5, 20, 100)
ball = GameSprite('Без имени1.png', 300, 200, 3, 65, 65)

clock = time.Clock()
FPS = 60

speed_x = 3
speed_y = 3

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.blit(background, (0, 0))
        racket1.update_l()
        racket2.update_r()

        GameSprite.draw_text(30, f"Score_1: {score1}", (255, 255, 255), (10, 50))
        GameSprite.draw_text(30, f"Score_2: {score2}", (255, 255, 255), (580, 50))

        # Движение мяча
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        # Отскок от левой/правой
        if ball.rect.y < 5 or ball.rect.y > 430:
            speed_y *= -1

        # Отскок от платформы — только если летел вниз
        if speed_y > 0 and ball.rect.colliderect(racket1.rect) or ball.rect.colliderect(racket2.rect):
            speed_x *= -1
        racket1.show()
        racket2.show()
        ball.show()

        if ball.rect.x > 700:
            ball.rect.x = 300
            ball.rect.y = 200
            score1 += 1
        
        if ball.rect.x < 0:
            ball.rect.x = 300
            ball.rect.y = 200
            score2 += 1

        if score1 == 10:
            window.blit(WIN1, (150, 200))  
            finish = True      

        if score2 == 10:
            window.blit(WIN2, (150, 200))  
            finish = True   

    display.update()
    clock.tick(FPS)
