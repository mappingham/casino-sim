import json
from pathlib import Path

# Repo root = parent of "casino" package folder
REPO_ROOT = Path(__file__).resolve().parent.parent

BANKROLL_PATH = REPO_ROOT / "data" / "bankroll.json"

def load_bankroll() -> int:
    with BANKROLL_PATH.open("r", encoding="utf-8") as f:
        data = json.load(f)
    return int(data.get("bankroll", 0))

def save_bankroll(bankroll: int) -> None:
    BANKROLL_PATH.parent.mkdir(parents=True, exist_ok=True)
    with BANKROLL_PATH.open("w", encoding="utf-8") as f:
        json.dump({"bankroll": int(bankroll)}, f, indent=2)