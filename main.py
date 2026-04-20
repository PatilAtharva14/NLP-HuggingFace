# main.py

import pygame
import time
from generator import generate_music

pygame.mixer.init()

def play_music(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def game_simulation():
    states = ["calm", "battle", "victory", "game_over"]

    for state in states:
        print(f"🎮 State: {state}")
        
        file = generate_music(state)
        play_music(file)

        time.sleep(8)  # play for few seconds

if __name__ == "__main__":
    print("Starting Game Music Generator...")
    game_simulation()