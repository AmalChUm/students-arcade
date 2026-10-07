"""
Anagram Checker Plugin for Students Arcade
"""

AUTHOR = "Merve Filiz Baker"
APP_NAME = "Anagram Checker"

def run():
    
    word1 = "listen"
    word2 = "silent"
    
    is_anagram = sorted(word1.lower()) == sorted(word2.lower())
    
    print(f"  🔤 Comparing '{word1}' and '{word2}'...")
    if is_anagram:
        print(f"  ✨ Result: They are anagrams!")
    else:
        print(f"  ❌ Result: They are not anagrams.")
    
    return ""