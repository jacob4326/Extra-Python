import pygame
import sys
import time

pygame.init()

WIDTH = 1200
HEIGHT = 940
screen = pygame.display.set_mode((WIDTH, HEIGHT))
menu_screen=pygame.Rect((WIDTH//4, HEIGHT//4, WIDTH//2, HEIGHT//2))
menu_on = False
icon = pygame.image.load("roshan.png")
pygame.display.set_caption("Despacito Simulator Ultimate Edition: Ultra Premium Deluxe Remasterd Bundle 2026")
pygame.display.set_icon(icon)

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

forest_color = (120, 170, 110)
market_color = (195, 140, 95)

scene = "Blast Off Center"
player_image=pygame.image.load("roshan.png")
player_image=pygame.transform.smoothscale(player_image, (100, 100))
player_rect = player_image.get_rect(topleft=(100, 200))
#player = pygame.image.load("roshan.png").get_rect(center=(200,200))
speed = 4


def draw_blastoffcenter():
    screen.fill((98, 141, 109))

def draw_carrotville():
    screen.fill((165, 118, 85))

def draw_ginnungagap():
    screen.fill((0,0,0))

def draw_menu():
    pygame.draw.rect(screen, (50, 50, 50), menu_screen)
    


def draw_player():
    # Draw player in a simple cartoon style
    #pygame.draw.rect(screen, (30, 100, 170), player)
    #pygame.draw.circle(screen, (255, 220, 180), (player.centerx, player.y + 12), 10)
    #pygame.draw.rect(screen, (235, 120, 80), (player.x + 5, player.y + 38, player.width - 10, 8))
    screen.blit(player_image, player_rect)

def draw_scene_label():
    label = font.render(scene.capitalize(), True, (255, 255, 230))
    screen.blit(label, (20, 15))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    dx = 0
    dy = 0
    if menu_on==False:
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx -= speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx += speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            dy -= speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy += speed
        if keys[pygame.K_LSHIFT]:
            speed=8
        else:
            speed=4

    # Move player and keep inside current screen.
    player_rect.x += dx
    player_rect.y += dy
    player_rect.x = max(0, min(player_rect.x, WIDTH - player_rect.width))
    player_rect.y = max(0, min(player_rect.y, HEIGHT - player_rect.height))

    # Scene switching by crossing screen boundaries.
    if scene == "Blast Off Center" and player_rect.right >= WIDTH:
        scene = "Carrotville"
        player_rect.x = 0
    elif scene == "Carrotville" and player_rect.left <= 0:
        scene = "Blast Off Center"
        player_rect.x = WIDTH - player_rect.width
    elif scene == "Carrotville" and player_rect.right >= WIDTH:
        scene = "ginnungagap"
        player_rect.x = 0
    elif scene == "ginnungagap" and player_rect.left <= 0:
        scene = "Carrotville"
        player_rect.x = WIDTH - player_rect.width

    # Draw current scene.
    if scene == "Blast Off Center":
        draw_blastoffcenter()
    elif scene == "Carrotville":
        draw_carrotville()
    elif scene == "market":
        draw_carrotville()
    elif scene == "ginnungagap":
        draw_ginnungagap()

    draw_player()
    draw_scene_label()

    if keys[pygame.K_ESCAPE]:
        if menu_on == True:
            menu_on = False
            time.sleep(0.15)
        else:
            menu_on = True
            time.sleep(0.15)
    if menu_on:
        draw_menu()


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
