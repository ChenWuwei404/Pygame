# Pygame
# lang = python

import pygame,sys
import win32api,win32con
from pygame.constants import MOUSEBUTTONDOWN
pygame.init()

window_x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
window_y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)# - 72

menutype = "start"
menuchose = 0
menuchosing = 1


screen = pygame.display.set_mode((window_x,window_y))
pygame.display.set_caption("乱斗三国")




#GUI load
background = pygame.image.load("bg.jpg")
te_logo = pygame.image.load("logo_w.png")
te_menu = pygame.image.load("menu.png")
me_new = pygame.image.load("menu_game.png")
me_chose = pygame.image.load("menu_chose.png")
me_gray = pygame.image.load("menu_gray.png")




#Button load
bu_game = pygame.image.load("button_game.png")
bu_chose = pygame.image.load("button_chose.png")
bu_back_w = pygame.image.load("button_back_w.png")
bu_back_b = pygame.image.load("button_back_b.png")






while True:
    mouse_x,mouse_y = pygame.mouse.get_pos()
    mouse_down = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            mouse_down = True
    screen.fill((255,255,255))
    if 0 <= mouse_x <= 320 and 50 <= mouse_y <= 98:
        menuchose = 1
        if mouse_down == True:
            menuchosing = 1
    elif 0 <= mouse_x <= 320 and 98 <= mouse_y <= 156:
        menuchose = 2
        if mouse_down == True:
            menuchosing = 2

    if menutype == "menu":
        screen.blit(background,(0,0))
        screen.blit(te_menu,(0,0))
        screen.blit(me_new,(0,0))
        screen.blit(bu_back_w,(0,0))
        if menuchose == 1:
            screen.blit(me_gray,(0,50))
        if menuchosing == 1:
            screen.blit(me_chose,(0,50))
        if menuchose == 2:
            screen.blit(me_gray,(0,98))
        if menuchosing == 2:
            screen.blit(me_chose,(0,98))
        if 0 <= mouse_x <= 48 and 0 <= mouse_y <= 32:
            screen.blit(bu_back_b,(0,0))
            if mouse_down == True:
                menutype = "start"
    
    
    if menutype == "start":
        screen.blit(background,(0,0))
        screen.blit(te_logo,(window_x-20-124,20))
        screen.blit(bu_game,(window_x-20-124,20+40+10))
        if window_x-20-124 <= mouse_x <=window_x-20  and  70 <= mouse_y <=103:
            screen.blit(bu_chose,(window_x-20-124,20+40+10))
            if mouse_down == True:
                menutype = "menu"
    pygame.display.update()
