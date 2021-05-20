import os
import pygame


class FileSystem:
    def __init__(self, start_name, input_dir, output_dir, output_name, blank=False):
        self.start_name = start_name
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.output_name = output_name
        self.blank = blank

        if self.blank:
            self.file_names = [self.output_name]
            self.idx = 0
            self.cur_img = None
        else:
            self.file_names = os.listdir(input_dir)
            self.idx = self.file_names.index(start_name)
            self.cur_img = None
            self.read_cur()
        return

    def read_cur(self):
        if self.blank:
            return self.cur_img
        file_name = os.path.join(self.input_dir, self.file_names[self.idx])
        self.cur_img = pygame.image.load(file_name)
        return

    def get_cur(self):
        return self.cur_img

    def get_next(self):
        if self.idx + 1 >= len(self.file_names):
            return None
        else:
            self.idx += 1
            self.read_cur()
        return self.get_cur()

    def save_img(self, canvas):
        file_name = os.path.join(self.output_dir, self.file_names[self.idx])
        pygame.image.save(canvas, file_name)
        return
