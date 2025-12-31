import pygame
import time
from random import randint


pygame.mixer.init()

BPM = 140
BEAT_TIME = 60 / BPM
notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

class Bar:
    def getFirstNote(self) -> int:
        if self.bass >= 5: return self.getNoteIndex(0)
        if self.bass >= 3: return self.getNoteIndex(1)
        return self.getNoteIndex(2)

    def getNoteIndex(self, n: int) -> int:
        return self.bass + 2 * randint(0, n)

    def getRandomNote(self) -> int:
        return randint(0, 6)

    def describe(self):
        print('bass', notes[self.bass] + '3')
        melody = ''
        for note in [self.note1, self.note2, self.note3, self.note4]:
            melody += notes[note] + '4 '
        print('melody', melody + '\n')


class SmoothBar(Bar):
    def __init__(self):
        self.bass = self.getRandomNote()
        self.note1 = self.getFirstNote()
        self.note2 = self.getStepNote(self.note1)
        self.note3 = self.getStepNote(self.note2)
        self.note4 = self.getStepNote(self.note3)

    def getStepNote(self, prev_note: int) -> int:
        step = randint(-1, 1)
        new_note = prev_note + step
        return max(0, min(new_note, 6))

class RandomBar(Bar):
    def __init__(self):
        self.bass = self.getRandomNote()
        self.note1 = self.getFirstNote()
        self.note2 = self.getRandomNote()
        self.note3 = self.getRandomNote()
        self.note4 = self.bass


class Program:
    def __init__(self):
        self.bass = []
        self.melody = []
        self.addNotesToList(self.bass, 'sound/bass/{}3.ogg')
        self.addNotesToList(self.melody, 'sound/melody/{}4.ogg')
        
    def addNotesToList(self, note_list: list, path: str):
        for note in notes:
            note_list.append(pygame.mixer.Sound(path.format(note)))

    def playBar(self, bar: Bar):
        self.bass[bar.bass].play()
        self.playAndWait(self.melody[bar.note1])
        self.playAndWait(self.melody[bar.note2])
        self.playAndWait(self.melody[bar.note3])
        self.playAndWait(self.melody[bar.note4])
    
    def playAndWait(self, sound: pygame.mixer.Sound):
        sound.play()
        time.sleep(BEAT_TIME)


if __name__ == '__main__':
    instance = Program()

    print('Press Ctrl+C to end the program.')
    try:
        while True:
            bar = SmoothBar()
            bar.describe
            instance.playBar(bar)
    except:
        pass
