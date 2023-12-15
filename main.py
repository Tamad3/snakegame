import pygame, sys, random
from pygame.math import Vector2

pygame.init()

GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24)

cell_size = 30
number_of_cells = 25

class Food:
 def __init__(self, food_surface):
     self.food_surface = food_surface
     self.position = self.generate_random_pos()

 def draw(self, screen):
     food_rect = pygame.Rect(self.position.x * cell_size, self.position.y * cell_size, cell_size, cell_size)
     screen.blit(self.food_surface, food_rect)

 def generate_random_pos(self):
     x = random.randint(0, number_of_cells - 1)
     y = random.randint(0, number_of_cells - 1)
     self.position = Vector2(x, y)
     return self.position

class Snake:
  def __init__(self):
      self.body = [Vector2(6,9), Vector2(5,9), Vector2(4,9)]

  def draw(self, screen):
      for segment in self.body:
          pygame.draw.rect(screen, GREEN, pygame.Rect(segment.x * cell_size, segment.y * cell_size, 0, 7))

screen = pygame.display.set_mode((cell_size*number_of_cells, cell_size*number_of_cells))
pygame.display.set_caption("Le Snake")
clock = pygame.time.Clock()
food_surface = pygame.image.load("Graphics/food.png")
food = Food(food_surface)
snake = Snake()

# Game loop
while True:
 for event in pygame.event.get():
     if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()

 screen.fill(GREEN)
 food.draw(screen)
 snake.draw(screen)
 pygame.display.update()
 clock.tick(60)
