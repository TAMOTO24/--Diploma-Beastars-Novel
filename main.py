import os
import pygame
from modules.structureClasses import MenuController
# from modules.structureClasses import ManualObjects
import router
import settings

pygame.init()
SIZEH, SIZEW = 500, 960

min_width, min_height = 500, 800

MC = MenuController()
screen = pygame.display.set_mode([SIZEW, SIZEH], pygame.RESIZABLE, vsync=1)  # Screen properties
pygame.display.set_caption('BEASTARS')

menuBG = pygame.image.load(r'assets/Background/Menu.jpg')
menuBG_obj = MC.structureBGSize(menuBG, SIZEW, SIZEH)

running = True
while running:
    mouseButtonDown = False

    screen.fill((0, 0, 0))#clear screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.VIDEORESIZE:
        #     pass
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseButtonDown = True
                

    CURRENTW, CURRENTH = pygame.display.get_window_size()
    mouse_pos = pygame.mouse.get_pos()
    screen = MC.setCentre(menuBG_obj, CURRENTW, CURRENTH, screen)
    menuBG_obj = MC.structureBGSize(menuBG, CURRENTW, CURRENTH)
    settingBtn = MC.button(5, "Settings", r'assets/Font/Fonstars-4Bo0p.otf')

    settingBtn['btn'] = MC.setObjCoordIncludeScale(
        CURRENTW, CURRENTH, settingBtn['btn'], 70, 15
    )

    startBtn = MC.button(5, "START", r'assets/Font/Fonstars-4Bo0p.otf')
    startBtn['btn'] = MC.setObjCoordIncludeScale(
        CURRENTW, CURRENTH, startBtn['btn'], 70, 5
    )

    if startBtn['btn'].collidepoint(mouse_pos) and mouseButtonDown:
       router.main(CURRENTW,  CURRENTH, screen)
       continue
    elif startBtn['btn'].collidepoint(mouse_pos):
        startBtn['text'] = MC.button(5, "START", r'assets/Font/Fonstars-4Bo0p.otf', textColor=(255, 0, 0))['text']

        
    if settingBtn['btn'].collidepoint(mouse_pos) and mouseButtonDown:
       settings.main(CURRENTW,  CURRENTH, screen)
       continue
    elif settingBtn['btn'].collidepoint(mouse_pos):
        settingBtn['text'] = MC.button(5, "SETTINGS", r'assets/Font/Fonstars-4Bo0p.otf', textColor=(255, 0, 0))['text']

    startBtn['surf'].blit(startBtn['text'], startBtn['textRect']) #set text in btn surface
    settingBtn['surf'].blit(settingBtn['text'], settingBtn['textRect'])
    
    screen.blit(startBtn['surf'], startBtn['btn'])
    screen.blit(settingBtn['surf'], settingBtn['btn'])
    pygame.display.flip()

pygame.quit()
