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

I tested three user profiles: High-Energy Pop (pop, happy, energy 0.9, valence 0.8), Chill Lofi (lofi, chill, energy 0.35, valence 0.6), and Deep Intense Rock (rock, intense, energy 0.92, valence 0.4). For each one I checked whether the top 5 matched what I would expect by ear and whether the "Because" reasons made sense. The biggest surprise was Storm Runner earning points in all four categories, which happened because my rock profile almost exactly matched its row in the data. I also expected Dusty Backroads to score higher for the pop profile, but it is a country song, so it cannot earn genre points and tops out at 4.0. Comparing profiles: High-Energy Pop and Chill Lofi had completely different results, with high-energy songs like Sunrise City for pop and low-energy songs like Library Rain for lofi, which makes sense because their energy targets are 0.9 and 0.35. Pop and Rock shared Gym Hero, because both profiles want high energy and Gym Hero is high energy with an intense mood. Lofi and Rock had no songs in common, as expected. As an experiment I halved the genre points and doubled the energy multiplier. It moved Fuego Nocturno above Gym Hero for the pop profile, but it also let an ambient song beat a lofi song for the lofi profile, so the change was different rather than clearly better.

---

## 8. Future Work

If I kept developing this, the first thing I would do is add more songs per genre, because genres with only one song cause the unfair gap I saw between users like the lofi and rock listeners. Second, I would group every genre into related families, not just pop with indie pop and lofi with ambient and jazz, so related genres earn partial credit for all users. Third, I would add a diversity rule so the top 5 can't be filled with near-identical songs, which would also help with the filter bubble problem. I would also let a user list more than one favorite genre or mood to handle more complex tastes.

---

## 9. Personal Reflection

I learned that recommenders turn data into predictions by comparing a song's attributes to what the user wants and turning each match into points, which gives every song a score that can be ranked. In my version, the four categories (genre, mood, energy, and valence) each add points, and sorting those scores produces the song rankings. Throughout this assignment it was clear that AI is a great tool that needs to be worked alongside rather than just left to do the work. For example, I first picked tempo as a category, but Claude's correlation check showed that it duplicates energy, so I switched to energy and added valence. I chose the weights genre 2.0, mood 1.5, energy 1.5, and valence 1.0, with partial credit for related categories. Something that surprised me was Storm Runner earning points in all four categories, and Dusty Backroads scoring far less than I expected because it is a country song and cannot earn genre points. Storm Runner finished far above every other rock song because my profile almost exactly matched it, which helped me see how a recommendation app could push certain songs heavily when they match a user's profile so well.
