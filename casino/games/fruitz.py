import random

SYMBOLS = ["🍒", "🍋", "🍊", "🍇", "🍉"]

def play(bankroll: int) -> int:
    print("\n=== Fruitz ===")
    print("Press Enter to spin ($1)")
    print("Type 'q' then Enter to quit\n")

    while True:
        if bankroll <= 0:
            print("No money left.")
            return bankroll

        cmd = input("Spin? ").strip().lower()
        if cmd == "q":
            print("Leaving Fruitz...\n")
            return bankroll

        bankroll -= 1

        reels = [
            random.choice(SYMBOLS),
            random.choice(SYMBOLS),
            random.choice(SYMBOLS),
        ]

        print(f"[ {' | '.join(reels)} ]")
        print(f"Bankroll: ${bankroll}\n")
