import pygame


class TextInputBox(pygame.sprite.Sprite):
    def __init__(self, x, y, w, font):
        super().__init__()
        self.color = (255, 255, 255)
        self.backcolor = None
        self.pos = (x, y)
        self.width = w
        self.font = font
        self.active = False
        self.text = ""
        self.render_text()

    def render_text(self):
        t_surf = self.font.render(self.text, True, self.color, self.backcolor)
        self.image = pygame.Surface((max(self.width, t_surf.get_width() + 10), t_surf.get_height() + 10),
                                    pygame.SRCALPHA)
        if self.backcolor:
            self.image.fill(self.backcolor)
        self.image.blit(t_surf, (5, 5))
        pygame.draw.rect(self.image, self.color, self.image.get_rect().inflate(-2, -2), 2)
        self.rect = self.image.get_rect(topleft=self.pos)

    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.active = self.rect.collidepoint(event.pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                elif event.key == pygame.K_BACKSPACE and self.active:
                    self.text = self.text[:-1]
                else:
                    if self.active and event.unicode in 'qazwsxedcrfvtgbyhnujmikolp.@_QAZWSXEDCRFVTGBYHNUJMIKOLP':
                        self.text += event.unicode
                self.render_text()


pygame.init()
window = pygame.display.set_mode((500, 200))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

text_input_box = TextInputBox(50, 50, 400, font)
text_input_box2 = TextInputBox(50,80,400,font)
group = pygame.sprite.Group(text_input_box)
group.add(text_input_box2)

run = True
while run:
    clock.tick(60)
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            run = False
    group.update(event_list)

    window.fill(0)
    group.draw(window)
    pygame.display.flip()

pygame.quit()
exit()
