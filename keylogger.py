import os
from pynput.keyboard import Listener

word_counts = {}
current_word = ""

target_word = input("Enter the word to track: ")

if os.path.exists("log.txt"):
    with open("log.txt", 'r') as f:
        log_content = f.read()
        current_word_count = log_content.split().count(target_word)
else:
    current_word_count = 0

word_counts[target_word] = current_word_count

def write_to_file(key):
    global current_word

    letter = str(key).replace("'", "")

    if letter == "Key.enter":
        letter = "\n"

    if letter in ['Key.space', 'Key.enter']:
        if current_word == target_word:
            word_counts[current_word] = word_counts.get(current_word, 0) + 1
            print(f"Real-time Count for '{target_word}': {word_counts[current_word]}")
        
        current_word = ""
    elif letter in ["Key.shift", "Key.shift_r", "Key.ctrl_l", "Key.ctrl_r"]:
        pass
    else:
        current_word += letter

    with open("log.txt", 'a') as f:
        f.write(letter if letter not in ["Key.space", "Key.enter"] else " ")

with Listener(on_press=write_to_file) as l:
    l.join()
