import numpy as np
from scipy import linalg

data = [
    {"Song Length": 240, "Extension Probability": 20, "Skip Next Probability": 5, "Extension Length": 30,
     "Skip Next if Extended": 10, "Royalty Fee": 5},
    {"Song Length": 300, "Extension Probability": 10, "Skip Next Probability": 40, "Extension Length": 30,
     "Skip Next if Extended": 50, "Royalty Fee": 3},
    {"Song Length": 210, "Extension Probability": 25, "Skip Next Probability": 10, "Extension Length": 60,
     "Skip Next if Extended": 30, "Royalty Fee": 3},
    {"Song Length": 235, "Extension Probability": 20, "Skip Next Probability": 20, "Extension Length": 30,
     "Skip Next if Extended": 20, "Royalty Fee": 4},
    {"Song Length": 350, "Extension Probability": 10, "Skip Next Probability": 50, "Extension Length": 20,
     "Skip Next if Extended": 50, "Royalty Fee": 5},
    {"Song Length": 185, "Extension Probability": 40, "Skip Next Probability": 20, "Extension Length": 90,
     "Skip Next if Extended": 10, "Royalty Fee": 3},
    {"Song Length": 220, "Extension Probability": 30, "Skip Next Probability": 10, "Extension Length": 30,
     "Skip Next if Extended": 10, "Royalty Fee": 3},
    {"Song Length": 320, "Extension Probability": 10, "Skip Next Probability": 5, "Extension Length": 20,
     "Skip Next if Extended": 5, "Royalty Fee": 3},
    {"Song Length": 260, "Extension Probability": 20, "Skip Next Probability": 0, "Extension Length": 60,
     "Skip Next if Extended": 0, "Royalty Fee": 5},
    {"Song Length": 480, "Extension Probability": 50, "Skip Next Probability": 0, "Extension Length": 120,
     "Skip Next if Extended": 0, "Royalty Fee": 8}
]

num_song = len(data)
num_states = num_song * 2
Q = np.zeros((num_states, num_states))

for i, song in enumerate(data):
    normal_state = i * 2
    extended_state = normal_state + 1

    song_len = song["Song Length"]
    extension_prob = song["Extension Probability"] / 100
    skip_prob = song["Skip Next Probability"] / 100
    ext_len = song["Extension Length"]
    skip_next_prob = song["Skip Next Probability"] / 100

    if extension_prob > 0:
        Q[normal_state, extended_state] = extension_prob / song_len

    # Transition from Normal to Next Song (no skip state)
    Q[normal_state, (normal_state + 2) % num_states] = (1 - extension_prob - skip_prob) / song_len

    # Transition from Extended to Next Song
    Q[extended_state, (normal_state + 2) % num_states] = (1 - skip_next_prob) / ext_len

    # Transition from Normal to Next Song if skipping
    if skip_prob > 0:
        Q[normal_state, (normal_state + 2) % num_states] += skip_prob / song_len

    # Transition from Extended to Next Song if skipping after extension
    if skip_next_prob > 0:
        Q[extended_state, (normal_state + 2) % num_states] += skip_next_prob / ext_len

# Normalize the diagonal
for row in range(num_states):
    Q[row, row] = -np.sum(Q[row])

Q2 = np.vstack((Q.T, np.ones(num_states)))
u = np.zeros(num_states + 1)
u[-1] = 1

pi = np.linalg.lstsq(Q2, u, rcond=None)[0]

songs_of_interest = {
    "Song 1": pi[0] + pi[1],
    "Song 2": pi[2] + pi[3],
    "Song 5": pi[8] + pi[9],
    "Song 9": pi[16] + pi[17],
    "Song 10": pi[18] + pi[19]
}

for song, prob in songs_of_interest.items():
    print(f"The probability of hearing {song} when entering randomly: {prob:.4f}")
