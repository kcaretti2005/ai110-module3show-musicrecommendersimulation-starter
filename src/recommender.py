import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

GENRE_GROUPS = [{"pop", "indie pop"}, {"lofi", "ambient", "jazz"}]
MOOD_GROUPS = [{"chill", "relaxed", "focused"}]

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    float_fields = ("energy", "tempo_bpm", "valence", "danceability", "acousticness")
    songs: List[Dict] = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            row["id"] = int(row["id"])
            for field in float_fields:
                row[field] = float(row[field])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons: List[str] = []

    def same_group(a: str, b: str, groups: List[set]) -> bool:
        return any(a in g and b in g for g in groups)

    # Genre: exact match or related genre
    song_genre = song["genre"].strip().lower()
    user_genre = user_prefs["genre"].strip().lower()
    if song_genre == user_genre:
        score += 2.0
        reasons.append("genre match (+2.0)")
    elif same_group(song_genre, user_genre, GENRE_GROUPS):
        score += 1.0
        reasons.append("related genre (+1.0)")

    # Mood: exact match or related mood
    song_mood = song["mood"].strip().lower()
    user_mood = user_prefs["mood"].strip().lower()
    if song_mood == user_mood:
        score += 1.5
        reasons.append("mood match (+1.5)")
    elif same_group(song_mood, user_mood, MOOD_GROUPS):
        score += 0.75
        reasons.append("related mood (+0.75)")

    # Energy: closer to the target earns more, up to 1.5
    energy_points = 1.5 * (1 - abs(song["energy"] - user_prefs["energy"]))
    if energy_points > 0:
        score += energy_points
        reasons.append(f"energy closeness (+{energy_points:.2f})")

    # Valence: closer to the target earns more, up to 1.0
    valence_points = 1.0 * (1 - abs(song["valence"] - user_prefs["valence"]))
    if valence_points > 0:
        score += valence_points
        reasons.append(f"valence closeness (+{valence_points:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        scored.append((song, score, explanation))

    ranked = sorted(scored, key=lambda item: item[1], reverse=True)
    return ranked[:k]
