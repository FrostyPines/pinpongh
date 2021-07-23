from pygame import*

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 115))
        self.y_speed = player_speed_y
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

w = 20
h = 17

win_height = 788
win_width = 1024

background = transform.scale(image.load("bgf2.png"), (1024,788))
window = display.set_mode((win_width, win_height))
display.set_caption("pinpongh1")

class Player(GameSprite):
    def move_player1(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.y_speed

        if keys_pressed[K_s] and self.rect.y < win_height - 115:
            self.rect.y += self.y_speed

    def move_player2(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.y_speed

        if keys_pressed[K_DOWN] and self.rect.y < win_height - 115:
            self.rect.y += self.y_speed

class Bilutza(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed_y, player_speed_x):
        super().__init__(player_image, player_x, player_y, player_speed_y)
        self.x_speed = player_speed_x
        self.image = transform.scale(image.load(player_image), (65, 65))

    def move(self):
        self.rect.y += self.y_speed
        self.rect.x += self.x_speed
        if self.rect.y >= win_height - 65:
            self.x_speed = self.x_speed
            self.y_speed = -self.y_speed
        if self.rect.x >= win_width - 65:
            self.x_speed = -self.x_speed
            self.y_speed = self.y_speed
        if self.rect.y <= 0:
            self.x_speed = self.x_speed
            self.y_speed = -self.y_speed
        if self.rect.x <= 0:
            self.x_speed = -self.x_speed
            self.y_speed = self.y_speed      
Player1 = Player("plat1.png", 20, win_height - 450, 5)
Player2 = Player("plat2.png", 934, win_height - 450, 5)
mingiutza = Bilutza("tenis_ball.png", win_width/2, win_height/2, 5, 5)

font.init()
font_ = font.SysFont('Arial', 70)
lose = font_.render('Partea Dreapta a Castigat!', True, (255, 0, 255  ))
lose1 = font_.render('Partea Stanga a Castigat!', True, (255, 0, 255  ))

score = 0

font.init()
sus_font = font.SysFont('Arial', 40)
text1 = sus_font.render("Score: " + str(score), True, (225, 225, 255))

finish = False
game = True

class Walls(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed_y):
        self.image = transform.scale(image.load(player_image), (35, 85))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.y_speed = player_speed_y

Wall1 = Walls("spikes1.png", 0, 0, 0)
Wall2 = Walls("spikes1.png", 0, 83, 0)
Wall3 = Walls("spikes1.png", 0, 166, 0)
Wall4 = Walls("spikes1.png", 0, 249, 0)
Wall5 = Walls("spikes1.png", 0, 332, 0)
Wall6 = Walls("spikes1.png", 0, 415, 0)
Wall7 = Walls("spikes1.png", 0, 498, 0)
Wall8 = Walls("spikes1.png", 0, 581, 0)
Wall9 = Walls("spikes1.png", 0, 664, 0)
Wall10 = Walls("spikes1.png", 0, 747, 0)
Wall11 = Walls("spikes.png", 988, 0, 0)
Wall12 = Walls("spikes.png", 988, 83, 0)
Wall13 = Walls("spikes.png", 988, 166, 0)
Wall14 = Walls("spikes.png", 988, 249, 0)
Wall15 = Walls("spikes.png", 988, 332, 0)
Wall16 = Walls("spikes.png", 988, 415, 0)
Wall17 = Walls("spikes.png", 988, 498, 0)
Wall18 = Walls("spikes.png", 988, 581, 0)
Wall19 = Walls("spikes.png", 988, 664, 0)
Wall20 = Walls("spikes.png", 988, 747, 0)

high_score = 0

with open("scoruletz.txt", "r", encoding = "utf-8") as file:
    high_score = file.readline()

text2 = sus_font.render("High Score: " + high_score, True, (225, 225, 255))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish == False:
        window.blit(background,(0, 0))
        window.blit(text1,(450, 50))
        window.blit(text2,(400, 10))

        mingiutza.reset()

        Player1.reset()
        Player2.reset()
        
        Wall1.reset()
        Wall2.reset()
        Wall3.reset()
        Wall4.reset()
        Wall5.reset()
        Wall6.reset()
        Wall7.reset()
        Wall8.reset()
        Wall9.reset()
        Wall10.reset()
        Wall11.reset()
        Wall12.reset()
        Wall13.reset()
        Wall14.reset()
        Wall15.reset()
        Wall16.reset()
        Wall17.reset()
        Wall18.reset()
        Wall19.reset()
        Wall20.reset()

        Player1.move_player1()
        Player2.move_player2()

        mingiutza.move()

        if sprite.collide_rect(Player2, mingiutza):
            mingiutza.x_speed = -mingiutza.x_speed
            score = score + 1
            text1 = sus_font.render("Score: " + str(score), True, (225, 225, 255))
            mingiutza.rect.x -= 8

        if sprite.collide_rect(Player1, mingiutza):
            mingiutza.x_speed = -mingiutza.x_speed
            score = score + 1
            text1 = sus_font.render("Score: " + str(score), True, (225, 225, 255))
            mingiutza.rect.x += 8

        if sprite.collide_rect(mingiutza, Wall1):
            finish = True
            window.blit(lose, (300, 300))
            
        if sprite.collide_rect(mingiutza, Wall2):
            finish = True
            window.blit(lose, (300, 300))

        if sprite.collide_rect(mingiutza, Wall3):
            finish = True
            window.blit(lose, (300, 300))

        if sprite.collide_rect(mingiutza, Wall4):
            finish = True
            window.blit(lose, (300, 300))

        if sprite.collide_rect(mingiutza, Wall5):
            finish = True
            window.blit(lose, (300, 300))

        if sprite.collide_rect(mingiutza, Wall6):
            finish = True
            window.blit(lose, (300, 300))

        if sprite.collide_rect(mingiutza, Wall7):
            finish = True
            window.blit(lose, (300, 300))

        if sprite.collide_rect(mingiutza, Wall8):
            finish = True
            window.blit(lose, (300, 300))

        if sprite.collide_rect(mingiutza, Wall9):
            finish = True
            window.blit(lose, (300, 300))

        if sprite.collide_rect(mingiutza, Wall10):
            finish = True
            window.blit(lose, (300, 300))

        if sprite.collide_rect(mingiutza, Wall11):
            finish = True
            window.blit(lose1, (300, 300))

        if sprite.collide_rect(mingiutza, Wall12):
            finish = True
            window.blit(lose1, (300, 300))

        if sprite.collide_rect(mingiutza, Wall13):
            finish = True
            window.blit(lose1, (300, 300))

        if sprite.collide_rect(mingiutza, Wall14):
            finish = True
            window.blit(lose1, (300, 300))

        if sprite.collide_rect(mingiutza, Wall15):
            finish = True
            window.blit(lose1, (300, 300))

        if sprite.collide_rect(mingiutza, Wall16):
            finish = True
            window.blit(lose1, (300, 300))

        if sprite.collide_rect(mingiutza, Wall17):
            finish = True
            window.blit(lose1, (300, 300))

        if sprite.collide_rect(mingiutza, Wall18):
            finish = True
            window.blit(lose1, (300, 300))

        if sprite.collide_rect(mingiutza, Wall19):
            finish = True
            window.blit(lose1, (300, 300))

        if sprite.collide_rect(mingiutza, Wall20):
            finish = True
            window.blit(lose1, (300, 300))

        if score > int(high_score):
            high_score = score
            text2 = sus_font.render("High Score: " + str(high_score), True, (225, 225, 255))
            with open("scoruletz.txt", "w", encoding = "utf-8") as file:
                file.write(str(high_score))

    display.update()
    time.delay(10)