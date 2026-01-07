from casino.storage import BANKROLL_PATH, load_bankroll, save_bankroll
from casino.games.fruitz import play


def main() -> None:
    bankroll = load_bankroll()
    bankroll = play(bankroll)

    
    print(f"Session ended. Bankroll saved: ${bankroll}")

if __name__ == "__main__":
    main()
