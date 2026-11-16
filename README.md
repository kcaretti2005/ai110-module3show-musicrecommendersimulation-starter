# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

## How The System Works

Real recommendation systems like Spotify and YouTube use two main approaches: collaborative filtering, which uses what other users liked and skipped, and content-based filtering, which uses song attributes. My version is content-based. `songs.csv` only has song attributes and no user history, so it takes a user's taste profile, scores every song against it, and ranks the results.

### Features
- **Song:** genre, mood, energy, valence
- **UserProfile:** favorite_genre, favorite_mood, target_energy, target_valence

I originally picked tempo, but Copilot showed that tempo, acousticness, and danceability all move almost in lockstep with energy (tempo and energy correlate at 0.96). Using them would count the same signal twice, so I dropped them. Valence is the one numeric feature that captures something different.

### Algorithm Recipe
Each song gets a score out of 6.0:
- **Genre (2.0):** full points for an exact match. Half credit for a related genre in the same group, for example pop and indie pop.
- **Mood (1.5):** full points for an exact match. Half credit for a similar mood, for example chill and relaxed.
- **Energy (1.5):** closeness to the user's target: 1.5 × (1 − |song energy − target|)
- **Valence (1.0):** closeness to the user's target, scored the same way.

The recommender scores every song in the catalog, sorts from highest to lowest, and returns the top k with the reasons for each score.

### Expected Biases
- Genre has the highest weight, so the system may over-prioritize genre and ignore great songs that match the user's mood.
- Valence only ranges from about 0.48 to 0.84 in my data, so it barely changes the ranking.
- Most genres only have one song, so genre alone can't fill a top-5 list.
- Content-based systems tend to create a filter bubble of more of the same.
---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



