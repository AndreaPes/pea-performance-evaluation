from collections import deque

import numpy as np

# Constants
T_MAX = 1200000
T_CASH = 20 * 60
PROB_LEAVE = 0.2
PROB_CASH = 0.35
PROB_CARD = 0.65

# GUI Time -> Hyper-Exponential
l1_hyper = 0.4
l2_hyper = 0.1
p1_hyper = 0.8

# Cash Payment -> Exponential
l_exp = 0.4

# Electronic Payment -> Erlang
k_erlang = 4
l_erlang = 2

# Printing -> Hyper-Erlang
p1_erlang = 0.95
k1_erlang = 2
k2_erlang = 1
l1_erlang = 10
l2_erlang = 0.1

# Ticket Pricing
urban_price = 2.5
urban_prob = 0.9
area1_price = 4
area1_prob = 0.06
area2_price = 6
area2_prob = 0.04

# Initialize state and time tracking
current_state = 1  # Start in GUI state
t = dt = next_state = 0
time_in_states = {'GUI': 0, 'Cash': 0, 'Electronic': 0, 'Printing': 0}
RTT = deque()
current_RTT = 0
balance = 0
print_cont = 0


def update_balance():
    u_balance = np.random.rand()
    if u_balance < urban_prob:
        return urban_price
    elif u_balance < (urban_prob + area1_prob):
        return area1_price
    else:
        return area2_price


while t < T_MAX:
    if current_state == 1:  # GUI

        if t != 0:
            RTT.append(current_RTT)
            current_RTT = 0

        u1_hyper, u2_hyper = np.random.rand(), np.random.rand()
        dt = np.where(u1_hyper < p1_hyper, -np.log(u2_hyper) / l1_hyper, -np.log(u2_hyper) / l2_hyper)
        time_in_states['GUI'] += dt

        current_RTT += dt  # Increment round-trip time
        next_state = 1 if np.random.rand() < PROB_LEAVE else (2 if np.random.rand() < PROB_CASH else 3)

    elif current_state == 2:  # Cash Payment

        dt = -np.log(np.random.rand()) / l_exp
        time_in_states['Cash'] += dt
        current_RTT += dt

        # Balance Update for Cash Payment
        balance += update_balance()

        next_state = 4  # Move to printing

    elif current_state == 3:  # Electronic Payment

        dt = -np.sum(np.log(np.random.rand(k_erlang))) / l_erlang
        time_in_states['Electronic'] += dt
        current_RTT += dt
        next_state = 4  # Move to printing

    elif current_state == 4:  # Printing

        u1_erlang = np.random.rand()
        dt = -np.sum(np.log(np.random.rand(k1_erlang if u1_erlang < p1_erlang else k2_erlang))) / (
            l1_erlang if u1_erlang < p1_erlang else l2_erlang)
        time_in_states['Printing'] += dt
        current_RTT += dt
        print_cont += 1
        next_state = 1  # Return to GUI

    # Update time and state
    t += dt
    current_state = next_state

# Display results
print("Probability of Waiting for GUI Input: ", time_in_states['GUI'] / t)
print("Probability of Cash Transaction: ", time_in_states['Cash'] / t)
print("Probability of Electronic Transaction: ", time_in_states['Electronic'] / t)
print("Probability of Printing: ", time_in_states['Printing'] / t)
print("Average Duration of a Transaction: ", np.mean(list(RTT)))
print("Average cash collected in 20 hours: ", balance / (T_MAX / T_CASH))
