from GameData import *


class Output:
    def __init__(self, base, canvas_color, bg_color, tool_space):
        self.base = base
        self.bg_color = bg_color
        self.tool_space = tool_space
        self.canvas_color = canvas_color

        self.paint_canvas = pygame.Surface((self.base.canvas_w, self.base.canvas_h))
        self.paint_canvas.fill(self.canvas_color)

        self.bg_canvas = pygame.Surface((self.base.canvas_w, self.base.canvas_h))
        self.bg_canvas.fill(self.canvas_color)
        self.set_alpha(self.bg_canvas, 80)
        self.bg_canvas_img = None

        self.menu_box = pygame.Surface((self.base.toolbar_w, self.base.toolbar_h))  # menuBox
        self.set_alpha(self.menu_box, 80)
        self.menu_box.fill(self.tool_space)

        # Used as background for the menu box
        self.menu_box_bg = pygame.Surface((self.base.toolbar_w, self.base.toolbar_h))
        self.menu_box_bg.fill(self.bg_color)

        self.ialpha = 150  # For the infobox
        self.info_box = pygame.Surface((self.base.infobox_w, self.base.infobox_h))
        self.set_alpha(self.info_box, self.ialpha)
        self.info_box.fill(self.bg_color)
        return

    def blit_canvas(self):
        self.blit_paint_canvas()
        self.blit_bg_canvas()
        return

    def clear_canvas(self):
        self.clear_paint_canvas()
        self.clear_bg_canvas()
        return

    def blit_paint_canvas(self):
        self.base.window.blit(self.paint_canvas, (self.base.canvas_x, self.base.canvas_y))
        return

    def clear_paint_canvas(self):
        self.paint_canvas.fill(self.canvas_color)
        return

    def blit_bg_canvas(self):
        if self.bg_canvas_img is not None:
            self.bg_canvas.blit(self.bg_canvas_img, (0, 0))
        self.base.window.blit(self.bg_canvas, (self.base.canvas_x, self.base.canvas_y))
        return

    def clear_bg_canvas(self):
        self.bg_canvas.fill(self.canvas_color)
        return

    def set_bg_canvas(self, img):
        self.bg_canvas_img = pygame.transform.scale(img, (self.base.canvas_w, self.base.canvas_h))
        return

    def blit_background(self):
        self.base.window.fill(self.bg_color)
        self.clear_canvas()
        self.blit_canvas()
        return

    def blit_menu(self):
        self.base.window.blit(self.menu_box_bg, (self.base.toolbar_x, self.base.toolbar_y))

        self.base.window.blit(self.menu_box, (self.base.toolbar_x, self.base.toolbar_y))
        self.base.window.blit(self.info_box, (self.base.infobox_x, self.base.infobox_y))

        self.info_box.fill(self.bg_color)
        return

    def set_alpha(self, rectangle, alpha_val=100):
        rectangle.set_alpha(alpha_val)
        return


class PaintData:
    def __init__(self):
        self.b_size = 10
        self.b_darkness = 0

        self.prime_color = Colors.water
        self.color = None
        self.set_color()
        return

    def set_color(self):
        self.color = tupadd(self.prime_color, int(self.b_darkness))
        return


class Painting:  # THE OUTPUT
    def __init__(self, output, paint_data):
        self.output = output
        self.paint_data = paint_data

        self.selected = None
        self.draw_list = []
        self.i = -1  # used for deletion
        self.cleaned_list = []

        self.undo_mode = False

        self.drawing = False
        self.last_mouse_pos = None

        self.mouse = None
        self.clicked = None
        return

    def insert_draw_list(self, mouse_pos, color, b_size):
        ret = []
        if self.drawing and self.last_mouse_pos is not None:
            while mouse_pos_distance(mouse_pos, self.last_mouse_pos) >= b_size:
                self.last_mouse_pos = forward_a_step(self.last_mouse_pos, mouse_pos, b_size * 0.5)
                ret.append([self.last_mouse_pos, color, b_size])
            ret.append([mouse_pos, color, b_size])
        else:
            ret.append([mouse_pos, color, b_size])
        self.last_mouse_pos = mouse_pos
        return ret

    def mouse_actions(self):
        self.mouse = pygame.mouse.get_pos()
        self.clicked = pygame.mouse.get_pressed()
        if self.clicked == (1, 0, 0):
            canvas_x_min = self.output.base.canvas_x
            canvas_x_max = self.output.base.canvas_x + self.output.base.canvas_w
            canvas_y_min = self.output.base.canvas_y
            canvas_y_max = self.output.base.canvas_y + self.output.base.canvas_h
            if canvas_x_min < self.mouse[0] < canvas_x_max \
                    and canvas_y_min < self.mouse[1] < canvas_y_max:  # Inside the canvas
                point_list = self.insert_draw_list(self.mouse, self.paint_data.color, int(self.paint_data.b_size))
                self.blit_list(point_list)
                self.draw_list.extend(point_list)
                self.drawing = True
            else:
                self.drawing = False
        else:
            self.drawing = False

        if self.undo_mode:
            self.undo()
        return

    def perform_functions(self):
        self.blit_default()

        if self.selected is not None:
            if self.selected.being_clicked:
                if self.selected.name == 'Brush Size +' and self.selected.name != 'Pencil':
                    self.paint_data.b_size += 0.1

                elif self.selected.name == 'Brush Size -' and self.selected.name != 'Pencil':
                    if self.paint_data.b_size > 0:
                        self.paint_data.b_size -= 0.1

                if self.selected.name == 'Lighten Brush':
                    if self.paint_data.b_darkness < 200:
                        self.paint_data.b_darkness += 1
                        self.paint_data.set_color()

                elif self.selected.name == 'Darken Brush':
                    if self.paint_data.b_darkness > -200:
                        self.paint_data.b_darkness -= 1
                        self.paint_data.set_color()

                if self.selected.name == 'Pencil':
                    self.paint_data.color = Colors.road_0
                    self.paint_data.b_size = 2

                elif self.selected.name == 'Brush':
                    self.paint_data.color = Colors.water
                    self.paint_data.b_size = 10

                elif self.selected.name == 'Eraser':
                    self.paint_data.color = self.output.canvas_color

                elif self.selected.name == 'Clear':
                    self.paint_data.b_size = 10
                    self.output.clear_canvas()
                    self.output.blit_canvas()
                    self.draw_list = []
        return

    def blit_default(self):  # Blitting stuff like brushsize
        message_to_screen(self.output.base.window, "Shade : " + str(int(self.paint_data.b_darkness * -1)),
                          Colors.coolyellow, 80, 455, 20)  # BrushDarkness
        message_to_screen(self.output.base.window, "Size : " + str(int(self.paint_data.b_size)), Colors.coolgreen, 80,
                          515, 20)  # BrushSize

        pygame.draw.circle(self.output.base.window, Colors.black, (135, 630),
                           int(self.paint_data.b_size) + 2)  # Outline
        pygame.draw.circle(self.output.base.window, self.paint_data.color, (135, 630),
                           int(self.paint_data.b_size))  # How the brushlooks
        return

    def blit_list(self, points):
        for point in points:
            cood = point[0]
            canvas_cood = (cood[0] - self.output.base.canvas_x, cood[1] - self.output.base.canvas_y)
            pygame.draw.circle(self.output.paint_canvas, self.paint_data.color, canvas_cood, int(self.paint_data.b_size))
        self.output.blit_canvas()
        return

    def blit(self, cood):
        canvas_cood = (cood[0] - self.output.base.canvas_x, cood[1] - self.output.base.canvas_y)
        pygame.draw.circle(self.output.paint_canvas, self.paint_data.color, canvas_cood, int(self.paint_data.b_size))
        self.output.blit_canvas()
        return

    def undo(self):
        if len(self.draw_list) > 0:
            self.draw_list.pop()

        self.output.clear_canvas()

        for point in self.draw_list:
            mouse_pos = point[0]
            canvas_cood = (mouse_pos[0] - self.output.base.canvas_x, mouse_pos[1] - self.output.base.canvas_y)
            pygame.draw.circle(self.output.paint_canvas, point[1], canvas_cood, point[2])

        self.output.blit_canvas()
        return

    def clear(self):
        self.draw_list = []
        return

    def clean_list(self):
        self.cleaned_list = []

        # Removing Duplicates
        for i in self.draw_list:
            if i not in self.cleaned_list:
                self.cleaned_list.append(i)

        print(len(self.draw_list))
        print(len(self.cleaned_list))
        return


class MyButton:
    def __init__(self, output, painting, image, x, y, size, grow, name='NONE', detail='Description',
                 color=Colors.coolblue, function=None):
        self.output = output
        self.painting = painting

        self.file = pygame.image.load(image)
        self.size = size
        self.grow = grow
        self.color = color
        self.name = name
        self.detail = [detail]

        self.image = pygame.transform.scale(pygame.image.load(image), (self.size, self.size))
        self.image.set_alpha(25)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.function = function
        self.being_clicked = False
        self.hovering = False

        self.mouse = None
        self.clicked = None
        return

    def display_button(self):
        self.mouse = pygame.mouse.get_pos()
        self.clicked = pygame.mouse.get_pressed()

        if self.rect.x < self.mouse[0] < self.rect.x + self.size \
                and self.rect.y < self.mouse[1] < self.rect.y + self.size:
            self.image = pygame.transform.scale(self.file, (self.grow, self.grow))
            self.output.base.window.blit(self.image,
                                         (self.rect.x - (self.grow - self.size) * 0.5,
                                          self.rect.y - (self.grow - self.size) * 0.5))

            message_to_screen(self.output.info_box, self.name, self.color,
                              0, 0.25 * self.output.base.infobox_h, 30, True)

            self.output.set_alpha(self.output.info_box, 200)  # MAKES THE INFO BOX DARKER

            if self.clicked != (1, 0, 0):
                self.hovering = True
                self.being_clicked = False
            elif self.clicked == (1, 0, 0) and self.hovering:
                self.painting.selected = self
                self.being_clicked = True
            else:
                self.being_clicked = False

        else:
            self.hovering = False

            self.image = pygame.transform.scale(self.file, (self.size, self.size))  # Change image to the original size
            self.output.base.window.blit(self.image, (self.rect.x, self.rect.y))  # Display the icon

            self.output.set_alpha(self.output.info_box, self.output.ialpha)  # makes the info box to the original color
        return


class ColorButton:  # Buttons
    def __init__(self, output, painting, color, x, y, size, grow, name):
        self.output = output
        self.painting = painting

        self.size = size
        self.grow = grow
        self.color = color
        self.name = name

        self.box = pygame.Surface((self.size, self.size))
        self.box.fill(self.color)

        self.rect = self.box.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.being_clicked = False
        self.hovering = False

        self.mouse = None
        self.clicked = None
        return

    def display_color(self):
        self.mouse = pygame.mouse.get_pos()
        self.clicked = pygame.mouse.get_pressed()

        if self.rect.x < self.mouse[0] < self.rect.x + self.size \
                and self.rect.y < self.mouse[1] < self.rect.y + self.size:
            self.box = pygame.Surface((self.grow, self.grow))
            self.box.fill(self.color)

            self.output.base.window.blit(self.box,
                                         (self.rect.x - (self.grow - self.size) * 0.5,
                                          self.rect.y - (self.grow - self.size) * 0.5))

            message_to_screen(self.output.info_box, self.name, self.color,
                              0, 0.25 * self.output.base.infobox_h, 30, True)

            if self.clicked != (1, 0, 0):
                self.hovering = True
                self.being_clicked = False
            elif self.clicked == (1, 0, 0) and self.hovering:
                self.painting.paint_data.prime_color = self.color
                self.painting.paint_data.b_darkness = 0

                self.painting.paint_data.set_color()

                self.being_clicked = True
            else:
                self.being_clicked = False

        else:
            self.hovering = False

            self.box = pygame.Surface((self.size, self.size))  # Change image to the original size
            self.box.fill(self.color)

            self.output.base.window.blit(self.box, (self.rect.x, self.rect.y))  # Display the icon
        return
