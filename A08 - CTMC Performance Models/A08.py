import numpy as np
from scipy import linalg

# Data Initialization
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

num_states = len(data) * 2
Q = np.zeros((num_states, num_states))

# Fill the transition rate matrix Q
for i, song in enumerate(data):
    normal_state, extended_state = i * 2, i * 2 + 1
    song_len, ext_len = song["Song Length"], song["Extension Length"]
    extension_prob = song["Extension Probability"] / 100
    skip_prob = song["Skip Next Probability"] / 100
    skip_next_prob = song["Skip Next if Extended"] / 100

    Q[normal_state, extended_state] = extension_prob / song_len
    Q[normal_state, (normal_state + 2) % num_states] = (1 - extension_prob - skip_prob) / song_len
    Q[normal_state, (normal_state + 4) % num_states] = skip_prob / song_len

    Q[extended_state, (normal_state + 2) % num_states] = (1 - skip_next_prob) / ext_len
    Q[extended_state, (normal_state + 4) % num_states] = skip_next_prob / ext_len

# Set the diagonal elements
np.fill_diagonal(Q, -np.sum(Q, axis=1))

# Solve the linear system to find the stationary distribution
Q2 = Q.copy()
Q2[:, 0] = 1
u = np.zeros(num_states)
u[0] = 1
pi = linalg.solve(Q2.T, u)

# Calculate the probabilities for the songs of interest
songs_of_interest_indices = {"Song 1": 0, "Song 2": 2, "Song 5": 8, "Song 9": 16, "Song 10": 18}
songs_of_interest = {song: pi[idx] + pi[idx + 1] for song, idx in songs_of_interest_indices.items()}

# Display the results
for song, prob in songs_of_interest.items():
    print(f"Probability of patron entering while {song} is being played: {prob}")

# Compute the average cost
average_cost = sum((pi[i * 2] + pi[i * 2 + 1]) * song["Royalty Fee"] for i, song in enumerate(data))
print(f"The average cost of the songs is: {average_cost} €")

# Compute RTLP
xi0 = np.zeros((num_states, num_states))
xi0[18, 0] = xi0[19, 0] = 1
RTLP = ((Q * xi0) @ np.ones(num_states)) @ pi

print("Number of shows per day: ", RTLP * 60 * 60 * 24)
print("Average duration of the show: ", 1 / (RTLP * 60))
