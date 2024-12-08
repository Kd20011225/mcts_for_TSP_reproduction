import numpy as np
import matplotlib.pyplot as plt

# Extended time slots
time_tsp_extended_more = [0, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000]

lkh3_extended_more = [100] * len(time_tsp_extended_more)  
att_gcn_extended_more = [20, 25, 23, 22, 21, 20, 19, 18, 18, 17]  
difusco_extended_more = [30, 40, 38, 37, 36, 35, 34, 33, 33, 32]  
dimes_extended_more = [15, 22, 21, 20, 19, 18, 18, 17, 16, 16]  
softdist_extended_more = [25, 30, 29, 28, 27, 26, 26, 25, 25, 24] 
utsp_extended_more = [10, 12, 11, 10, 10, 9, 9, 8, 8, 8]  

# Plotting the extended graph
plt.figure(figsize=(12, 6))
plt.plot(time_tsp_extended_more, lkh3_extended_more, label="LKH-3", color="blue", marker='o')
plt.plot(time_tsp_extended_more, att_gcn_extended_more, label="ATT-GCN", color="orange", marker='s')
plt.plot(time_tsp_extended_more, difusco_extended_more, label="DIFUSCO", color="green", marker='^')
plt.plot(time_tsp_extended_more, dimes_extended_more, label="DIMES", color="red", marker='x')
plt.plot(time_tsp_extended_more, softdist_extended_more, label="SoftDist", color="purple", marker='d')
plt.plot(time_tsp_extended_more, utsp_extended_more, label="UTSP", color="brown", marker='v')

# Adding labels, title, and legend
plt.title("TSP 10000 with default MCTS setting", fontsize=14)
plt.xlabel("Time (s)", fontsize=12)
plt.ylabel("Score (%)", fontsize=12)
plt.grid(True)
plt.legend(loc="best", fontsize=10)

plt.show()