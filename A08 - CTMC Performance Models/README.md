# DJ Concert Analysis
___

### Overview

This report examines the performance of a DJ at a concert, where each song is played according to certain rules regarding extension, skipping, and continuation. The DJ has a playlist of 10 songs, each with specific characteristics like length, extension probability, and royalty fees. The analysis aims to evaluate various performance metrics of the concert based on the playlist behavior.

The following metrics are analyzed:

1. The probability that a patron hears a specific song when randomly entering the concert.
2. The average cost of songs played during a concert.
3. The number of shows that could be played per day and the average duration of each concert.

---

### Song Characteristics

| Song No. | Length (sec) | Extension Probability | Skip Next Probability | Extension Length (sec) | Skip Next if Extended | Royalty Fee (€) |
|----------|--------------|-----------------------|-----------------------|------------------------|-----------------------|------------------|
| 1        | 240          | 20%                   | 5%                    | 30                     | 10%                   | 5                |
| 2        | 300          | 10%                   | 40%                   | 30                     | 50%                   | 3                |
| 3        | 210          | 25%                   | 10%                   | 60                     | 30%                   | 3                |
| 4        | 235          | 20%                   | 20%                   | 30                     | 20%                   | 4                |
| 5        | 350          | 10%                   | 50%                   | 20                     | 50%                   | 5                |
| 6        | 185          | 40%                   | 20%                   | 90                     | 10%                   | 3                |
| 7        | 220          | 30%                   | 10%                   | 30                     | 10%                   | 3                |
| 8        | 320          | 10%                   | 5%                    | 20                     | 5%                    | 3                |
| 9        | 260          | 20%                   | 0%                    | 60                     | 0%                    | 5                |
| 10       | 480          | 50%                   | 0%                    | 120                    | 0%                    | 8                |

---

### Results

#### 1. Probability of Hearing a Specific Song
The probability that a patron hears a specific song when randomly entering the concert:

- **Song 1**: <span style="color:lightgreen;font-weight:bold">9.61%</span>
- **Song 2**: <span style="color:lightgreen;font-weight:bold">11.01%</span>
- **Song 5**: <span style="color:lightgreen;font-weight:bold">10.78%</span>
- **Song 9**: <span style="color:lightgreen;font-weight:bold">10.10%</span>
- **Song 10**: <span style="color:lightgreen;font-weight:bold">21.10%</span>

#### 2. Average Cost of Songs
The average royalty cost for the songs played during the concert:

- **Average Cost of Songs**: <span style="color:lightgreen;font-weight:bold">4.749 €</span>

#### 3. Number of Shows Per Day
The number of shows that could be played per day, assuming continuous play and immediate restarting of the show after completion:

- **Number of Shows Per Day**: <span style="color:lightgreen;font-weight:bold">33.76</span>
- **Average Duration of a Show**: <span style="color:lightgreen;font-weight:bold">42.65 minutes</span>

---

### Python Script

Python script that calculates all the above values and performs the analysis: [**A08.py**](A08.py)
