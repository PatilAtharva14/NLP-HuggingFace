import os
import random

OUTPUT_DIR = "assets/music"
os.makedirs(OUTPUT_DIR, exist_ok=True)

states = {
    "calm": "soft ambient peaceful music",
    "battle": "intense battle music",
    "victory": "happy victory music",
    "game_over": "sad emotional music"
}

# fallback files (your existing ones)
fallback_files = {
    "calm": "assets/calm.wav",
    "battle": "assets/battle.wav",
    "victory": "assets/victory.wav",
    "game_over": "assets/game_over.wav"
}

def generate_music(state):
    print(f"🎵 AI (lite) generating for: {state}")

    file_path = os.path.join(OUTPUT_DIR, f"{state}.wav")

    # simulate variation by randomly picking fallback
    source_file = fallback_files.get(state)

    if not os.path.exists(source_file):
        source_file = "assets/sample.wav"

    # randomize slightly (simulate AI variation)
    new_name = f"{state}_{random.randint(1,1000)}.wav"
    file_path = os.path.join(OUTPUT_DIR, new_name)

    import shutil
    shutil.copy(source_file, file_path)

    return file_path