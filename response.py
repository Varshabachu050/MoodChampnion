# response.py

def get_quote(mood: str, score: int) -> str:
    mood_quotes = {
        "happy": [
            "Keep spreading joy!",
            "Your happiness lights the world!"
        ],
        "sad": [
            "It's okay to feel sad. Brighter days are coming.",
            "Storms don’t last forever."
        ],
        "lonely": [
            "You are never truly alone.",
            "Connection starts with self-love."
        ],
        "tired": [
            "Rest is productive too.",
            "Recharge and rise stronger."
        ],
        "angry": [
            "Breathe in calm, breathe out anger.",
            "Strength is controlling emotions."
        ],
        "calm": [
            "Peace begins within.",
            "Stillness is power."
        ]
    }

    if score > 70:
        return mood_quotes[mood][0]
    return mood_quotes[mood][1]