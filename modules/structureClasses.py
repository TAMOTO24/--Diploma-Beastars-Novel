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
    def setNewScaledSize(self, width, height):
        new_width =  self.new_width * width//100
        new_height = self.new_height * height//100
        

        return (new_width, new_height)

    
    def setObjCoordIncludeScale(self, width, height, rect, moveX=0, moveY=0):
        x = width - self.new_width
        y = height - self.new_height

        if moveX > 0:
            moveX =  int(self.new_width * moveX/100) # procent of width
        if moveY > 0:
            moveY =  int(self.new_height * moveY/100) # procent of height

        # set coord 0,0 including screen scale (and add user X, Y to move on screen)
        coordX = ((x // 2) + moveX)
        coordY = ((y // 2) + moveY)

        # coordX = max(moveX, coordX)
        # coordY = max(moveY, coordY)

        rect.topleft = (coordX, coordY)

        return rect
    def drawBorder(self, rect, surf, color=(0, 0, 0), size=2, alpha=255, border_radius=0):
        color_with_alpha = (*color, alpha)
        
        if border_radius > 0:
            temp_surface = pygame.Surface(rect.size, pygame.SRCALPHA)
            pygame.draw.rect(temp_surface, color_with_alpha, (0, 0, rect.width, rect.height), border_radius)

            surf.blit(temp_surface, rect.topleft)
        else:
            pygame.draw.rect(surf, color_with_alpha, (0, 0, rect.width, rect.height), size)


    def setButtonImage(self, screen, path, rect, img_coord=(0, 0)):
        image = pygame.image.load(path)
        image_part_rect = pygame.Rect(rect)
        scaled_image = pygame.transform.scale(image, (self.new_width, self.new_height))

        if rect.width < 0:
            rect.width = abs(rect.width)
        if rect.height < 0:
            rect.height = abs(rect.height)

        if img_coord:
            image_part_rect.topleft = img_coord

        screen.blit(scaled_image, rect.topleft, area=image_part_rect)
    def setChapterTheme(self, rect, surf, text="Locked"):
        size = int(self.new_width * 3 / 100)
        font = pygame.font.SysFont('Comic Sans MS', size)

        text_surface = font.render(text, True, (0, 0, 0))
        text_width, text_height = text_surface.get_size()

        padlock = pygame.image.load(r'assets/Background/padlock.png')
        padlock_width, padlock_height = 30, 33 
        scaled_padlock = pygame.transform.scale(padlock, (padlock_width, padlock_height))

        button_height = max(text_height, padlock_height) + 10 
        button_surface = pygame.Surface((rect.width, button_height), pygame.SRCALPHA)
        button_surface.fill((150, 150, 150, 125))

        centreX = (scaled_padlock.width//2 - text_width - 5) + rect.width//2
        centreY = button_surface.get_height() // 2 -  scaled_padlock.get_height() // 2

        button_surface.blit(scaled_padlock, (centreX, centreY))
    
        text_centreX = button_surface.get_width() // 2 - text_width//2 + 10
        text_centreY = button_surface.get_height() // 2 - text_height//2
        button_surface.blit(text_surface, (text_centreX, text_centreY))

        surf.blit(button_surface, (0, 40))

    def button(self, TXTsize, text="button text", fontPath='Comic Sans MS',
                textColor=(0, 0, 0), alpha=0, surfX=1, surfY=1,
                  textAlign='center', width=0, padlockIMG=False):
        size = int(self.new_width * TXTsize/100)
        try:
            font = pygame.font.Font(fontPath, size)
        except: 
            font = pygame.font.SysFont(fontPath, size)

        text = font.render(text, 1, textColor)
        text_width, text_height = text.get_size()

        if width > 0:
            text_width = self.new_width * width//100
        if surfX > 0:
            surfX = self.new_width * surfX//100
        if surfY > 0:
            surfY = self.new_height * surfY//100

        # Set the button sizes to match the text
        button_surface = pygame.Surface((text_width + surfX, text_height + surfY), pygame.SRCALPHA) # +20 for indents

        button_surface.fill((150, 150, 150, alpha))

        if textAlign == 'center':
            text_rect = text.get_rect(
                center=(button_surface.get_width() /2, 
                button_surface.get_height()/2))
        elif textAlign == 'bottom':
            text_rect = text.get_rect(
                centerx=(button_surface.get_width() / 2), 
                bottom=button_surface.get_height() 
            )
        button_rect = button_surface.get_rect()

        if padlockIMG:
            self.setChapterTheme(button_rect, button_surface)

        return {'text': text,'textRect' : text_rect, 'btn' : button_rect, 'surf' : button_surface}