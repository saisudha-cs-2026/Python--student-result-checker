# Student Result Checker by Pasupuleti Sai Sudha
# B.Sc Computer Science - 5th Sem Python Grade: O
# Phone + Pydroid లో చేసిన Project

def check_pass(mark):
    if mark >= 35:
        return "Pass"
    else:
        return "Fail"

marks = [80, 30, 45]
print("--- Student Result Report ---")
for m in marks:
    result = check_pass(m)
    print("Mark:", m, "→", result)
