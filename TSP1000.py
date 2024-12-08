import numpy as np
import matplotlib.pyplot as plt

# Extended time slots for TSP-500
time_tsp_500_extended = np.linspace(0, 1000, 15)

# Adjusted and properly downward-curved scores for each method
lkh3_500_downward_corrected = [100] * len(time_tsp_500_extended)  # Baseline remains constant
att_gcn_500_downward_corrected = 30 - 60 * (1 - np.exp(-0.005 * time_tsp_500_extended))  # Downward exponential
difusco_500_downward_corrected = 30 - 55 * (1 - np.exp(-0.004 * time_tsp_500_extended))  # Downward exponential slower
dimes_500_downward_corrected = 30 - 50 * (1 - np.exp(-0.0045 * time_tsp_500_extended))  # Slightly varied downward
softdist_500_downward_corrected = 30 - 52 * (1 - np.exp(-0.0042 * time_tsp_500_extended))  # Smooth downward decay
utsp_500_downward_corrected = 30 - 30 * (1 - np.exp(-0.007 * time_tsp_500_extended))  # Steeper downward curve

# Plotting TSP-500 with extended time slots and properly downward curves
plt.figure(figsize=(10, 6))
plt.plot(time_tsp_500_extended, lkh3_500_downward_corrected, label="LKH-3", color="blue", marker='o')
plt.plot(time_tsp_500_extended, att_gcn_500_downward_corrected, label="ATT-GCN", color="orange", marker='s')
plt.plot(time_tsp_500_extended, difusco_500_downward_corrected, label="DIFUSCO", color="green", marker='^')
plt.plot(time_tsp_500_extended, dimes_500_downward_corrected, label="DIMES", color="red", marker='x')
plt.plot(time_tsp_500_extended, softdist_500_downward_corrected, label="SoftDist", color="purple", marker='d')
plt.plot(time_tsp_500_extended, utsp_500_downward_corrected, label="UTSP", color="brown", marker='v')

# Adding labels and title
plt.title("TSP-1000 with Default MCTS setting", fontsize=14)
plt.xlabel("Time (s)", fontsize=12)
plt.ylabel("Score (%)", fontsize=12)
plt.grid(True)
plt.legend(loc="best", fontsize=10)

plt.show()