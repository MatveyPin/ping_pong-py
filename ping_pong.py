import pygame

ground = (0, 204, 255)
window = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Пінг-понг")
      
game = True
clock = pygame.time.Clock()
fps = 60

while game:
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
            
    
    pygame.display.update() 
            
    clock.tick(fps)
