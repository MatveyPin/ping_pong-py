import pygame

ground = (0, 204, 255)
window = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Пінг-понг")

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_height):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
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

game = True
clock = pygame.time.Clock()
fps = 60
finish = False

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
    
    pygame.display.update() 
            
    clock.tick(fps)