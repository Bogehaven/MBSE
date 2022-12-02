import numpy as np
import matplotlib.pyplot as plt

baseline = np.genfromtxt('./results/pollution_history_baseline.csv', delimiter=',')
ev_10 = np.genfromtxt('./results/pollution_history_ev10.csv', delimiter=',')
ev_15 = np.genfromtxt('./results/pollution_history_ev15.csv', delimiter=',')
ev_20 = np.genfromtxt('./results/pollution_history_ev20.csv', delimiter=',')
ev_59 = np.genfromtxt('./results/pollution_history_ev54.csv', delimiter=',')
trucks_baseline = np.genfromtxt('./results/pollution_history_trucks_baseline.csv', delimiter=',')
trucks_ev_20 = np.genfromtxt('./results/pollution_history_trucks_ev20.csv', delimiter=',')
time = np.arange(len(ev_59))

plt.plot(time, baseline, label='Baseline')
plt.plot(time, ev_10, label='EV 10')
plt.plot(time, ev_15, label='EV 15')
plt.plot(time, ev_20, label='EV 20')
plt.plot(time, ev_59, label='EV 54')
plt.plot(time, trucks_ev_20, label='Trucks EV 20')
plt.plot(time, trucks_baseline, label='Trucks baseline')
plt.xlabel("Timetep")
plt.ylabel("Total NOx")
plt.title("Total NOx over time, no wind")
plt.legend()
plt.show()
#plt.savefig("./plots/cooling_schedule.png")
#plt.clf() #clear

s_trucks_ev_20 = np.genfromtxt('./results/pollution_sampled_trucks_ev20.csv', delimiter=',')
s_baseline = np.genfromtxt('./results/pollution_sampled_baseline.csv', delimiter=',')
s_ev54 = np.genfromtxt('./results/pollution_sampled_ev54.csv', delimiter=',')
time = np.arange(len(s_baseline))

plt.plot(time, s_baseline, label='Baseline')
plt.plot(time, s_ev54, label='EV 54')
plt.plot(time, s_trucks_ev_20, label='Trucks EV 20')
plt.xlabel("Timetep")
plt.ylabel("Total NOx")
plt.title("Total NOx over time, no wind")
plt.legend()
plt.show()
#plt.savefig("./plots/cooling_schedule.png")
#plt.clf() #clear
