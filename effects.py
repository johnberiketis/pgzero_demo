import os
from pygame import draw, Surface, Rect, Color, image
from pgzero import game
from utils import world

class Effect():

    def __init__(self, frames, pos, frames_duration):
        self.pos = pos
        self.frames_counter = 0
        self.index_counter = 1
        self.end_frame = frames_duration - 1
        self.frames = frames
        self.current_frame = frames[0]
        if len(frames) > 1:
            self.next_frame = frames[1]
        else:
            self.next_frame = None
        self.surface = image.load(self.current_frame["image"])
        world.add_effect(self)

    def update(self):

        if self.frames_counter == self.end_frame:
            world.remove_effect(self)
        elif self.next_frame:
            if self.frames_counter == self.next_frame["frame_number"]:
                self.index_counter += 1
                self.current_frame = self.next_frame
                self.surface = image.load(self.current_frame["image"])
                if self.index_counter < len(self.frames):
                    self.next_frame = self.frames[self.index_counter]
                else:
                    self.next_frame = None

        self.frames_counter += 1
        

    def draw(self):
        game.screen.blit(self.surface, self.pos)

def explosion(pos):
    frames = [
        {"frame_number" : 0, "image" : "C:\\Users\\JackPoulis\\Desktop\\CoderDojo\\pgzero\\pgzero_demo\\images\\effects\\explosion1.png"},
        {"frame_number" : 3, "image" : "C:\\Users\\JackPoulis\\Desktop\\CoderDojo\\pgzero\\pgzero_demo\\images\\effects\\explosion2.png"},
        {"frame_number" : 5, "image" : "C:\\Users\\JackPoulis\\Desktop\\CoderDojo\\pgzero\\pgzero_demo\\images\\effects\\explosion3.png"},
        {"frame_number" : 8, "image" : "C:\\Users\\JackPoulis\\Desktop\\CoderDojo\\pgzero\\pgzero_demo\\images\\effects\\explosion4.png"},
        {"frame_number" : 10, "image" : "C:\\Users\\JackPoulis\\Desktop\\CoderDojo\\pgzero\\pgzero_demo\\images\\effects\\explosion5.png"}
    ]
    duration = 15

    Effect(frames, pos, duration)