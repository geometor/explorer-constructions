'''copy to session folder and run from there.'''
from sessions import *


def main():
    MUSIC = True
    TICK = True
    root = pm.N.E3
    octaves = 3
    scale_type = pm.S.pentatonic_major

    scale = pm.build_scale(
        root=root, 
        scale_type=scale_type, 
        octaves=octaves)

    bpm = 120
    tempo = int(pm.bpm2tempo(bpm))

    #  build_session('.', scale, tempo, tick=TICK, music=MUSIC)
    build_sequence('.', scale, tempo, tick=TICK, music=MUSIC)


if __name__ == '__main__':
    main()


