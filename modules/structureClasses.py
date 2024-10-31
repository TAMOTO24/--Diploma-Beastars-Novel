import pygame

class MenuController:
    def __init__(self):
        pygame.init()

    def structureBGSize(self, obj, width, height): #Scale object to screen size

        original_width, original_height = obj.get_size()

        scale_factor = min(width / original_width, height / original_height)

        self.new_width = int(original_width * scale_factor)
        self.new_height = int(original_height * scale_factor)

        obj = pygame.transform.scale(obj, (self.new_width, self.new_height))

        return obj
    
    def setCentre(self, obj, width, height, screen):

        obj_width, obj_height = obj.get_size()
        
        screen.blit(obj, (((width - obj_width) // 2), ((height - obj_height) // 2)))

        return screen
    
    def setObjCoordIncludeScale(self, width, height, obj, rect, moveX=0, moveY=0):
        x = width - self.new_width
        y = height - self.new_height

        if moveX > 0:
            moveX =  int(self.new_width * moveX//100) # procent of width
        if moveY > 0:
            moveY =  int(self.new_height * moveY//100) # procent of height

        # set coord 0,0 including screen scale (and add user X, Y to move on screen)
        coordX = ((x // 2) + moveX) - obj.get_width() // 2
        coordY = ((y // 2) + moveY) - obj.get_height() // 2

        rect.topleft = (coordX, coordY)

        return rect
    
    def button(self, TXTsize, text="button text", fontPath='Comic Sans MS', textColor=(0, 0, 0), alpha=0, surfX=20, surfY=20):
        size = int(self.new_width * TXTsize/100)
        try:
            font = pygame.font.Font(fontPath, size)
        except: 
            font = pygame.font.SysFont(fontPath, size)

        text = font.render(text, 1, textColor)
        text_width, text_height = text.get_size()

        # Set the button sizes to match the text
        button_surface = pygame.Surface((text_width + surfX, text_height + surfY), pygame.SRCALPHA) # +20 for indents
            # button_surface = pygame.Surface((text_width + 20, text_height + 20), pygame.SRCALPHA) # +20 for indents
        button_surface.fill((150, 150, 150, alpha))

        text_rect = text.get_rect(
            center=(button_surface.get_width() /2, 
            button_surface.get_height()/2))
        
        button_surface.blit(text, text_rect)
        button_rect = button_surface.get_rect()

        return {'text': text,'textRect' : text_rect, 'btn' : button_rect, 'surf' : button_surface}