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

## 5. Strengths

The system works best when a user's taste is clear and the catalog has several songs that fit it. The Chill Lofi profile got excellent results, with Library Rain, Midnight Coding, and Focus Flow all at the top, and every one matched what I would have picked by ear. The partial credit also worked: for the High-Energy Pop profile, Rooftop Lights (indie pop) came in second behind Sunrise City because it earned related-genre credit plus a mood match. Because every score comes with a "Because" explanation, I could see exactly why each song ranked where it did and catch problems, like Gym Hero scoring well on genre alone.

---

## 6. Limitations and Bias

The biggest weakness I found is that the system treats users differently depending on how many songs of their genre are in the catalog. For the Chill Lofi profile the #1 and #2 songs are only 0.15 points apart (6.00 vs 5.85), but for Deep Intense Rock the gap is 2.08 points (5.90 vs 3.82). That is because rock has only one song, so none of the other songs earn genre or related-genre points, while lofi has three songs plus related genres (ambient and jazz) that earn partial credit. Genre also carries the biggest weight, so Gym Hero ranked above a happy-mood song for the pop profile on genre points alone. Valence only ranges from about 0.33 to 0.88, so it barely changes the ranking, and the system ignores things like lyrics, language, and artist.

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
