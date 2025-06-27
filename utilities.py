import os
import json

def check_collision(pos1, pos2):
    return pos1 == pos2

HIGHSCORE_FILE = "highscore.json"
MAX_ENTRIES = 10

def load_all_highscores():
    if not os.path.exists(HIGHSCORE_FILE):
        return {"normal": [], "blitz": [], "inverted": []}
    with open(HIGHSCORE_FILE, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {"normal": [], "blitz": [], "inverted": []}

def save_all_highscores(data):
    with open(HIGHSCORE_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def add_score(mode, name, score):
    data = load_all_highscores()
    if mode not in data:
        data[mode] = []
    data[mode].append({"name": name, "score": score})
    data[mode] = sorted(data[mode], key=lambda x: x['score'], reverse=True)[:MAX_ENTRIES]
    save_all_highscores(data)

def get_high_score(mode):
    data = load_all_highscores()
    if mode in data and data[mode]:
        return data[mode][0]["score"]
    return 0

def get_leaderboard(mode):
    data = load_all_highscores()
    return data.get(mode, [])