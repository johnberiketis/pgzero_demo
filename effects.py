import os
from pygame import draw, Surface, Rect, Color, image
from pgzero.actor import Actor
from pgzero import game
from utils import world

class Effect(Actor):

    def __init__(self, frames, pos, frames_duration):
        self.frames_counter = 0
        self.index_counter = 1
        self.end_frame = frames_duration - 1
        self.frames = frames
        self.current_frame = frames[0]
        if len(frames) > 1:
            self.next_frame = frames[1]
        else:
            self.next_frame = None
        super().__init__(self.current_frame["image"],  pos)
        world.add_effect(self)

    def update(self):

        if self.frames_counter == self.end_frame:
            world.remove_effect(self)
        elif self.next_frame:
            if self.frames_counter == self.next_frame["frame_number"]:
                self.index_counter += 1
                self.current_frame = self.next_frame
                self.image = self.current_frame["image"]
                if self.index_counter < len(self.frames):
                    self.next_frame = self.frames[self.index_counter]
                else:
                    self.next_frame = None

        self.frames_counter += 1
        

def explosion(pos):
    frames = [
        {"frame_number" : 0, "image" : "effects/explosion1"},
        {"frame_number" : 3, "image" : "effects/explosion2.png"},
        {"frame_number" : 5, "image" : "effects/explosion3.png"},
        {"frame_number" : 8, "image" : "effects/explosion4.png"},
        {"frame_number" : 10, "image" : "effects/explosion5.png"}
    ]
    duration = 15

    Effect(frames, pos, duration)