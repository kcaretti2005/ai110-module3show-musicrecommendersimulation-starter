# 🎵 Music Recommender Simulation

## Project Summary

What my version does essentially is it recommends music in an optimal way based off of genre, mood, energy, and valence. What my version does it assigns a weight to each one of those 4 and then basically give each song a score based off how it stacks up. For example a song can end with a score of 3.75 after having mood match = 1.5 points, energy closeness = 1.24 points, and valence closeness = 1.00 point. 

## How The System Works

Real recommendation systems like Spotify and YouTube use two main approaches: collaborative filtering, which uses what other users liked and skipped, and content-based filtering, which uses song attributes. My version is content-based. `songs.csv` only has song attributes and no user history, so it takes a user's taste profile, scores every song against it, and ranks the results.

### Features
- **Song:** genre, mood, energy, valence
- **User taste profile (a dictionary in main.py):** genre, mood, energy, valence

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
- Valence only ranges from about 0.33 to 0.88 in my data, so it barely changes the ranking.
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
   ```
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
```
User profile: genre = pop, mood = happy, energy = 0.8, valence = 0.8

Top recommendations:

Sunrise City - Score: 5.93
Because: genre match (+2.0), mood match (+1.5), energy closeness (+1.47), valence closeness (+0.96)

Rooftop Lights - Score: 4.93
Because: related genre (+1.0), mood match (+1.5), energy closeness (+1.44), valence closeness (+0.99)

Gym Hero - Score: 4.27
Because: genre match (+2.0), energy closeness (+1.30), valence closeness (+0.97)

Fuego Nocturno - Score: 3.84
Because: mood match (+1.5), energy closeness (+1.43), valence closeness (+0.92)

Dusty Backroads - Score: 3.75
Because: mood match (+1.5), energy closeness (+1.24), valence closeness (+1.00)
```
## Experiments You Tried

### Three profile tests (original weights: genre 2.0, energy 1.5)

### Experiment: weight shift
I changed genre points from 2.0 to 1.0 and changed the energy multiplier from 1.5 to 3.0 . As a result, Fuego Nocturno moved from #4 to #3 for the High-Energy Pop profile. This made the recommendations different with mixed accuracy: it helped the High-Energy Pop profile by pushing Gym Hero below Fuego Nocturno, but it hurt the Chill Lofi profile because an ambient song (Spacewalk Thoughts) now beat a lofi song (Focus Flow). The top 5 all now get 2.6 to 3.0 energy points which means the system mostly finds songs with similar energy.
```
=== High-Energy Pop ===

Sunrise City - Score: 5.84
Because: genre match (+2.0), mood match (+1.5), energy closeness (+1.38), valence closeness (+0.96)

Rooftop Lights - Score: 4.78
Because: related genre (+1.0), mood match (+1.5), energy closeness (+1.29), valence closeness (+0.99)

Gym Hero - Score: 4.42
Because: genre match (+2.0), energy closeness (+1.46), valence closeness (+0.97)

Fuego Nocturno - Score: 3.84
Because: mood match (+1.5), energy closeness (+1.42), valence closeness (+0.92)

Dusty Backroads - Score: 3.59
Because: mood match (+1.5), energy closeness (+1.09), valence closeness (+1.00)


=== Chill Lofi ===

Library Rain - Score: 6.00
Because: genre match (+2.0), mood match (+1.5), energy closeness (+1.50), valence closeness (+1.00)

Midnight Coding - Score: 5.85
Because: genre match (+2.0), mood match (+1.5), energy closeness (+1.40), valence closeness (+0.96)

Focus Flow - Score: 5.17
Because: genre match (+2.0), related mood (+0.75), energy closeness (+1.42), valence closeness (+0.99)

Spacewalk Thoughts - Score: 4.84
Because: related genre (+1.0), mood match (+1.5), energy closeness (+1.40), valence closeness (+0.95)

Coffee Shop Stories - Score: 4.11
Because: related genre (+1.0), related mood (+0.75), energy closeness (+1.47), valence closeness (+0.89)


=== Deep Intense Rock ===

Storm Runner - Score: 5.90
Because: genre match (+2.0), mood match (+1.5), energy closeness (+1.48), valence closeness (+0.92)

Iron Tide - Score: 3.82
Because: mood match (+1.5), energy closeness (+1.43), valence closeness (+0.90)

Concrete Crown - Score: 3.76
Because: mood match (+1.5), energy closeness (+1.38), valence closeness (+0.88)

Pulse Reactor - Score: 3.66
Because: mood match (+1.5), energy closeness (+1.44), valence closeness (+0.72)

Gym Hero - Score: 3.61
Because: mood match (+1.5), energy closeness (+1.48), valence closeness (+0.63)
```
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



