import perfect_pangram

text_correct = "Blowzy night-frumps vex'd Jack Q."
if perfect_pangram.perfect_pangram(text_correct):
    print("Perfect Pangram")
else:
    print("Not a perfect pangram")

text_incorrect = "aabbccddeeffgghijklmnopqrstuvwxyz"
if perfect_pangram.perfect_pangram(text_incorrect):
    print("Perfect Pangram")
else:
    print("Not a perfect pangram")

try:
    perfect_pangram.perfect_pangram(123)
except perfect_pangram.PangramError as e:
    print("Caught custom error:", e)

