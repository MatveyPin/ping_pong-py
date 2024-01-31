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

game = True
clock = pygame.time.Clock()
fps = 60

while game:
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
            
    
    pygame.display.update() 
            
    clock.tick(fps)
