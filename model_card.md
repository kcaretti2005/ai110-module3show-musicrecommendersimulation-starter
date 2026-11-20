# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**VibeMatch 1.0**

---

## 2. Intended Use

VibeMatch suggests songs from a small catalog based on a user's taste profile: a favorite genre, a favorite mood, a target energy level, and a target valence (how positive the song feels). It assumes the user can describe their taste with those four things and that one profile is enough, so it has no listening history. This is a classroom project for learning how recommenders work. It is not meant for real users.

---

## 3. How the Model Works

Every song in the catalog gets a score out of 6.0 based on how well it matches the user's profile. A genre match is worth 2.0 points, and a related genre (like pop and indie pop) earns half. A mood match is worth 1.5, and a similar mood (like chill and relaxed) earns half. Energy is worth up to 1.5 points and valence up to 1.0, and the closer a song is to the user's target, the more points it gets. The songs are then sorted from highest score to lowest and the top five are shown, each with a short "Because" list explaining where its points came from. The starter code only had empty functions, so I wrote the file loading, the scoring rule, and the ranking. I added valence as a feature, partial credit for related genres and moods, and the explanations.

---

## 4. Data

The catalog has 20 songs. I started with 10 and used an AI assistant to add 10 more in different genres, so there are 17 genres in total, from pop, lofi, rock, and jazz to hip hop, classical, country, reggae, and Latin. The moods are happy, chill, relaxed, focused, moody, and intense. Most genres have only one song, and lofi is the only one with three. Each song also has tempo, danceability, and acousticness, but I didn't use them because they move almost in lockstep with energy. Taste factors like lyrics, language, artist familiarity, and the time of day aren't in the data at all.

---
## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
