#создай игру "Лабиринт"!
from pygame import*

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed=player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a]and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d]and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_w]and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s]and self.rect.y < win_width - 80:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT]and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT]and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP]and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN]and self.rect.y < win_width - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = 'left'
    def update (self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= win_width - 85:
            self.direction = 'left'


        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Enemy2(GameSprite):
    direction = 'left'
    def update (self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= win_width - 85:
            self.direction = 'left'


        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self,color_1,color_2,color_3,wall_x,wall_y,wall_width,wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width,self.height))
        self.image.fill((color_1, color_2, color_3))
        #должен хранить свойство rect - прямоугольник
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



win_width = 700
win_height = 500
window = display.set_mode((win_width,win_height))
display.set_caption('Maze')
background = transform.scale(image.load('background.jpg'),(win_width,win_height))

player = Player('hero.png',5,win_height-80,5)
player2 = Player2('hero.png',5,350,5)
cyborg = Enemy('cyborg.png',600,300,5)
cyborg2 = Enemy('cyborg.png',500,200,5)
gold = GameSprite('treasure.png',550 ,400,0)

w1 = Wall(190, 178, 218, 110, 10, 450, 10)
w2 = Wall(190, 178, 218, 110, 100, 10, 300)

game = True
clock = time.Clock()
FPS = 60
finish=False

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

font.init()
font = font.SysFont('Arial',70)
win = font.render('YOU WIN!', True,(255,215,0))
lose = font.render('YOU LOOSE!', True,(180,0,0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game=False

    if finish != True:
        window.blit(background,(0,0))

        player.update()
        player.reset()
        player2.update()
        player2.reset()   

        cyborg.update()
        cyborg.reset()
        cyborg2.update()
        cyborg2.reset()

        gold.reset()
        w1.draw_wall()
        w2.draw_wall()

        if sprite.collide_rect(player,cyborg) or sprite.collide_rect(player2,cyborg2) or sprite.collide_rect(player,cyborg2) or sprite.collide_rect(player2,cyborg) or sprite.collide_rect(player,w1) or sprite.collide_rect(player2,w1) or sprite.collide_rect(player2,w2) or sprite.collide_rect(player,w2) :
            finish = True
            window.blit(lose,(200,200))
            kick.play()

        if sprite.collide_rect(player,gold) and sprite.collide_rect(player2,gold):
            finish = True
            window.blit(win,(200,200))
            money.play()

    display.update()
    clock.tick(FPS)