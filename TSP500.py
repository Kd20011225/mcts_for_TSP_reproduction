import matplotlib.pyplot as plt

time_tsp_500 = [0, 5, 10, 20, 100, 200, 500, 1000]
lkh3_500 = [100, 100, 100, 100, 100, 100, 100, 100]  
att_gcn_500 = [8, 7, 5, 3, 2, 1, 0, 0]  
difusco_500 = [50, 30, 25, 21, 10, 3, 1, 0]  
dimes_500 = [8, 8, 6, 3, 2, 1, 0, 0]  
softdist_500 = [9, 9, 7, 3, 2, 1, 0, 0]  
utsp_500 = [5, 3, 2, 1, 0, 0, 0, 0]  

# Plotting TSP-500 with default MCTS settings
plt.figure(figsize=(8, 6))
plt.plot(time_tsp_500, lkh3_500, label="LKH-3", color="blue", marker='o')
plt.plot(time_tsp_500, att_gcn_500, label="ATT-GCN", color="orange", marker='s')
plt.plot(time_tsp_500, difusco_500, label="DIFUSCO", color="green", marker='^')
plt.plot(time_tsp_500, dimes_500, label="DIMES", color="red", marker='x')
plt.plot(time_tsp_500, softdist_500, label="SoftDist", color="purple", marker='d')
plt.plot(time_tsp_500, utsp_500, label="UTSP", color="brown", marker='v')

# Adding labels and title
plt.title("TSP-500 with default MCTS settings", fontsize=14)
plt.xlabel("Time (s)", fontsize=12)
plt.ylabel("Score (%)", fontsize=12)
plt.grid(True)
plt.legend(loc="best", fontsize=10)

plt.show()