import pygame
import time

pygame.font.init()

ground = (0, 204, 255)
window = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Пінг-понг")

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_height):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.speed_x = 4
        self.speed_y = 4
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

class Player(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= self.speed 
        if keys[pygame.K_s] and self.rect.y < 435:
            self.rect.y += self.speed 
    def update1(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed 
        if keys[pygame.K_DOWN] and self.rect.y < 435:
            self.rect.y += self.speed 
        
ball = GameSprite("tennis_ball.png", 200, 200, 4, 50, 50)  
player1 = Player("platform.png", 20, 200, 7, 100, 50)
player2 = Player("platform.png", 320, 200, 7, 100, 50)  

font = pygame.font.SysFont("Arial", 26)
text = font.render("Player2 won", True, (255, 0, 0))
text2 = font.render("Player1 won", True, (255, 0, 0))
none = font.render("Нічия", True, (255, 0, 0))
game = True
clock = pygame.time.Clock()
fps = 60
finish = False
start_time = time.time()

while game:
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False

    if finish != True:
        window.fill(ground)
        player1.reset()
        player2.reset()
        player1.update()
        player2.update1()
        ball.reset()

        timee = 60 - (time.time() - start_time)
        seconds = int(timee % 60)
        time_text = font.render("Час:" + str(seconds), True, (255, 255, 255))
        window.blit(time_text, (290, 10))

        if ball.rect.y < -20 or ball.rect.y >= 430:
            ball.speed_y = -ball.speed_y
        if ball.rect.x < -75:
            window.blit(text, (270, 250))
            finish = True
        if ball.rect.x > 675:
            window.blit(text2, (270, 250))
            finish = True
        if pygame.sprite.collide_rect(ball, player1) or pygame.sprite.collide_rect(ball, player2):
            ball.speed_x = -ball.speed_x
            ball.speed_y = -ball.speed_y
        if seconds == 0:
            finish = True
            window.blit(none, (270, 250))
    
    pygame.display.update() 
            
    clock.tick(fps)
