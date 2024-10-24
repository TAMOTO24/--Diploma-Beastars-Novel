import os
import pygame
from modules.structureClasses import MenuController
# from modules.structureClasses import ManualObjects

pygame.init()
SIZEH, SIZEW = 920, 1360

min_width, min_height = 500, 800

MC = MenuController()
screen = pygame.display.set_mode([SIZEW, SIZEH], pygame.RESIZABLE, vsync=1)  # Screen properties
pygame.display.set_caption('BEASTARS')

menuBG = pygame.image.load(r'assets/Background/Menu.jpg')
menuBG_obj = MC.structureBGSize(menuBG, SIZEW, SIZEH)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEORESIZE:
            menuBG_obj = MC.structureBGSize(menuBG, event.w, event.h)
                

    CURRENTW, CURRENTH = pygame.display.get_window_size()
    mouse_pos = pygame.mouse.get_pos()
    screen = MC.setCentre(menuBG_obj, CURRENTW, CURRENTH, screen)

    startBtn = MC.button(5, "START", r'assets/Font/Fonstars-4Bo0p.otf')
    startBtn['btn'] = MC.setObjCoordIncludeScale(
        CURRENTW, CURRENTH, startBtn['surf'], startBtn['btn'], 85, 9
    )

    if startBtn['btn'].collidepoint(mouse_pos):
        startBtn['text'] = MC.button(5, "START", r'assets/Font/Fonstars-4Bo0p.otf', textColor=(255, 0, 0))['text']

    startBtn['surf'].blit(startBtn['text'], startBtn['textRect']) #set text in btn surface
    
    screen.blit(startBtn['surf'], startBtn['btn'])
    pygame.display.flip()

pygame.quit()
