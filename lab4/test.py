import perfect_pangram
import rational

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


r1 = rational.Rational(1, 2)
r2 = rational.Rational(1, 3)

print("r1:", r1)
print("r2:", r2)

r3 = r1 + r2
print("r1 + r2 =", r3)