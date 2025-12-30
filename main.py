import pygame
import time
from random import randint


pygame.mixer.init()

BMP = 140
BEAT_TIME = 60 / BMP
BAR_TIME = BEAT_TIME * 4
QUATER_BEAT_TIME = BEAT_TIME / 4


def getRandomNote() -> int:
    return randint(0, 6)


class Bar:
    def __init__(self):
        self.bass = getRandomNote()
        self.note1 = self.getFirstNote()
        self.note2 = getRandomNote()
        self.note3 = getRandomNote()
        
    def getFirstNote(self) -> int:
        if self.bass >= 5:
            return self.getNoteIndex(0)
        if self.bass >= 3:
            return self.getNoteIndex(1)
        return self.getNoteIndex(2)

    def getNoteIndex(self, n: int) -> int:
        return self.bass + 2 * randint(0, n)


class Program:
    def __init__(self):
        self.notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

        self.bass = []
        self.melody = []
        self.addNotesToList(self.bass, 'sound/bass/{}3.ogg')
        self.addNotesToList(self.melody, 'sound/melody/{}4.ogg')
        
    def addNotesToList(self, list: list, path: str):
        for note in self.notes:
            list.append(pygame.mixer.Sound(path.format(note)))

    def playBar(self, bar: Bar):
        self.playAndWait(self.bass[bar.bass], QUATER_BEAT_TIME)
        self.playAndWait(self.melody[bar.note1], BEAT_TIME)
        self.playAndWait(self.melody[bar.note2], BEAT_TIME)
        self.playAndWait(self.melody[bar.note3], BEAT_TIME)
        self.playAndWait(self.melody[bar.bass], QUATER_BEAT_TIME * 3)
    
    def playAndWait(self, sound: pygame.mixer.Sound, waiting_time: float):
        sound.play()
        time.sleep(waiting_time)


if __name__ == '__main__':
    instance = Program()

    print('Press Ctrl+C to end the program.')
    while True:
        instance.playBar(Bar())
