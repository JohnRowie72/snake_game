import os

def check_collision(pos1, pos2):
    return pos1 == pos2

def load_high_score(filename="highscore.txt"):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            try:
                return int(f.read().strip())
            except:
                return 0
    return 0

def save_high_score(score, filename="highscore.txt"):
    with open(filename, 'w') as f:
        f.write(str(score))