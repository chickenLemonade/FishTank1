import pygame
import random

pygame.init()

# Clock to set framerate
clock = pygame.time.Clock()

screen_info = pygame.display.Info()

screen_size = (width, height) = (screen_info.current_w, screen_info.current_h)

fish_image = pygame.image.load("fish.png")
fish_image = pygame.transform.smoothscale(fish_image, (70, 120))

fish_rect = fish_image.get_rect()
fish_rect.center = (width//2, height//2)

#variles to move fish
speed = pygame.math.Vector2(30, 5)
rotation = random.randint(0, 360)
speed.rotate_ip(rotation)

pygame.transform.rotate(fish_image, 180 - rotation)

screen = pygame.display.set_mode(screen_size)
color = (53, 255, 250)

#defines what happens when we move the fish
def move_fish():
  global fish_image
  screen_info = pygame.display.Info()
  fish_rect.move_ip(speed)

  #  IF FISH HITS TOP OR BOTTOM
  if fish_rect.top < 0 or fish_rect.bottom > screen_info.current_h:
    speed[1] *= -1
    fish_rect.move_ip(0, speed[1])
    fish_image = pygame.transform.flip(fish_image, True, False)

  #  IF FISH HITS LEFT OR RIGHT
  if fish_rect.left < 0 or fish_rect.right > screen_info.current_w:
    speed[0] *= -1
    fish_rect.move_ip(speed[0], 0)
    fish_image = pygame.transform.flip(fish_image, False, True)


def main():
  while True:
    clock.tick(60)
    move_fish()
    screen.fill(color)
    screen.blit(fish_image, fish_rect)
    pygame.display.flip()


if __name__ == '__main__':
  main()