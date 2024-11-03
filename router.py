import pygame
from modules.structureClasses import MenuController

def main(SIZEW, SIZEH, screen):
    MC = MenuController()

    line = "chapter 1;chapter 2;chapter 3"

    words = line.split(';')

    menuBG = pygame.image.load(r'assets/Background/Preview1.png')
    menuBG_obj = MC.structureBGSize(menuBG, SIZEW, SIZEH)

    btnList = []

    running = True
    while running:
        mouseButtonDown = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.VIDEORESIZE:
                menuBG_obj = MC.structureBGSize(menuBG, event.w, event.h)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseButtonDown = True
        CURRENTW, CURRENTH = pygame.display.get_window_size()        
        mouse_pos = pygame.mouse.get_pos()
        screen = MC.setCentre(menuBG_obj, CURRENTW, CURRENTH, screen)

        index = 0
        for i in words:
            index += 1
            obj = MC.button(4, i, alpha=100, surfX=150, surfY=0)
            obj['btn'] = MC.setObjCoordIncludeScale(
                CURRENTW, CURRENTH, obj['surf'], obj['btn'], 50, 10 * index
            )
            # btnList.append(obj)
            if obj['btn'].collidepoint(mouse_pos) and mouseButtonDown:
                print(i)
            if obj['btn'].collidepoint(mouse_pos):
                obj['text'] = MC.button(4, i, alpha=100, surfX=150, surfY=0, textColor=(255, 0, 49))['text']
                obj['surf'].blit(obj['text'], obj['textRect'])

            screen.blit(obj['surf'], obj['btn'])

        pygame.display.flip()