import random

def generate_code():
    digits = list("0123456789")
    random.shuffle(digits)
    return digits[:3]

def get_clues(code, guess):
    clues = []
    for i in range(3):
        if guess[i] == code[i]:
            clues.append("Match")
        elif guess[i] in code:
            clues.append("Close")
        else:
            clues.append("Nope")
    return clues

def main():
    print("🔐 Welcome to Code Breaker!")
    print("A 3-digit secret code has been generated. All digits are unique.\n")

    print("🧠 Clue Guide:")
    print("  Match → correct digit, correct place")
    print("  Close → correct digit, wrong place")
    print("  Nope  → digit not in code at all\n")

    code = generate_code()
    attempts = 0

    while True:
        guess_input = input("Your guess: ").strip()
        if len(guess_input) != 3 or not guess_input.isdigit():
            print("❌ Please enter exactly 3 digits.\n")
            continue

        guess = list(guess_input)
        attempts += 1

        if guess == code:
            print(f"🎉 You broke the code {''.join(code)} in {attempts} attempts!")
            break

        clues = get_clues(code, guess)
        print(f"\n🔎 Clues for your guess '{guess_input}':")
        for i in range(3):
            print(f"  ➤ Digit {i+1} ({guess[i]}): {clues[i]}")
        print("-" * 35 + "\n")

if __name__ == "__main__":
    main()