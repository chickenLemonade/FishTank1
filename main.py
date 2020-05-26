import pygame

pygame.init()

screen_info = pygame.display.Info()

# set size of game board to screen size
screen_size = (width, height) = (screen_info.current_w, screen_info.current_h)


# set screen to screen size
screen = pygame.display.set_mode(screen_size)

color = (53, 230, 250)

def main():
  while True:
    screen.fill(color)
    pygame.display.flip()




if __name__ == '__main__':
  main()