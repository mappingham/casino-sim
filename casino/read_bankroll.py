import json

def read_bankroll() -> None:
    with open("data/bankroll.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    bankroll = data.get("bankroll", 0)
    print(f"Current Bankroll: ${bankroll}")

if __name__ == "__main__":
    read_bankroll()