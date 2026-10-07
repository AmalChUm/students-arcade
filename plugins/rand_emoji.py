import random

AUTHOR = "Jenna Yasin"
APP_NAME = "Random Emoji"

EMOJIS = [
    ("💃", "(dancing lady)"), 
    ("😭", "(loudly crying)"), 
    ("🙏", "(folded hands)"), 
    ("🙄", "(face with rolling eyes)"), 
    ("❤️", "(red heart)"), 
    ("😂", "(face with tears of joy)"),
    ("😒", "(unamused face)"),
    ("🥳", "(partying face)")
]

def run():
    emoji, label = random.choice(EMOJIS)
    return f"Your {APP_NAME}: {emoji} {label}"
