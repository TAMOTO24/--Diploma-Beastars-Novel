import pygame
from modules.structureClasses import MenuController
import pygame_gui

def setElementScale(MC, manager, CURRENTW, CURRENTH, element, x, y, Text="Text"):
    
    a = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(0, 0, 200, 50),
        text=Text,
        manager=manager,
    )
    element.kill()
    a.set_dimensions(MC.setNewScaledSize(20, 10))
    a.set_relative_position(MC.setObjCoordIncludeScale(CURRENTW, CURRENTH, element.relative_rect, x, y,))

    return a

def main(SIZEW, SIZEH, screen):
    MC = MenuController()

    line = "I;II;III"

    words = line.split(';')

    menuBG = pygame.image.load(r'assets/Background/Preview1.png')
    menuBG_obj = MC.structureBGSize(menuBG, SIZEW, SIZEH)

    manager = pygame_gui.UIManager((SIZEW, SIZEH), 'theme.json')
    clock = pygame.time.Clock()

    btn_size = MC.setNewScaledSize(20, 10)

    button_back = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(0, 0, btn_size[0], btn_size[1]),  # Позиция и размер кнопки "Back"
        text='Back',
        manager=manager
    )

    button_select = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(0, 0, btn_size[0], btn_size[1]),  # Позиция и размер кнопки "Select"
        text='Select',
        manager=manager
    )

    running = True
    while running:
        time_delta = clock.tick(60) / 1000.0 
        mouseButtonDown = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.VIDEORESIZE:
                menuBG_obj = MC.structureBGSize(menuBG, event.w, event.h)
                manager.set_window_resolution((event.w, event.h))

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseButtonDown = True
        CURRENTW, CURRENTH = pygame.display.get_window_size()
        
        mouse_pos = pygame.mouse.get_pos()
        screen = MC.setCentre(menuBG_obj, CURRENTW, CURRENTH, screen)

        index = 0
        w = 0
        for i in words:
            index += 1
            if i == 'I':
                obj = MC.button(6, i, alpha=100, surfX=0, surfY=50, width=25, textAlign='bottom')
            else:
                obj = MC.button(6, i, alpha=100, surfX=0, surfY=50, width=25, textAlign='bottom', padlockIMG=True)
            
            if index == 1: # chapter width
                w += 8
            else:
                w += 30

            obj['btn'] = MC.setObjCoordIncludeScale(
                CURRENTW, CURRENTH, obj['btn'], w, moveY=5
            )
            # btnList.append(obj)
            if obj['btn'].collidepoint(mouse_pos) and mouseButtonDown and i == 'I':
                print(i)
            if obj['btn'].collidepoint(mouse_pos) and i == 'I':
                
                obj['text'] = MC.button(6, i, alpha=0, surfX=0, surfY=0, textColor=(255, 0, 49), textAlign='bottom')['text']
                obj['surf'] = MC.button(6, i, alpha=50, surfX=0, surfY=50, width=25, textAlign='bottom')['surf']
                MC.drawBorder(obj['btn'], obj['surf'], (255, 0, 49), 3) # draw border
            else:
                MC.drawBorder(obj['btn'], obj['surf'])

            obj['surf'].blit(obj['text'], obj['textRect'])
            if index == 1:
                MC.setButtonImage(screen, r'assets/Background/Room701Grouph.png', obj['btn'], img_coord=(50,50))
            screen.blit(obj['surf'], obj['btn'])
        
        button_back = setElementScale(MC, manager, CURRENTW, CURRENTH, button_back, 20, 70)
        button_select = setElementScale(MC, manager, CURRENTW, CURRENTH, button_select, 50, 70)

        manager.update(time_delta)
        manager.draw_ui(screen)

        pygame.display.flip()