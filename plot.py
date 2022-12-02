import numpy as np
import matplotlib.pyplot as plt

basedir = "./results_nowind/"

baseline = np.genfromtxt(basedir + 'pollution_history_cars_baseline.csv', delimiter=',')
ev_10 = np.genfromtxt(basedir + 'pollution_history_cars_ev10.csv', delimiter=',')
#ev_15 = np.genfromtxt(basedir + 'pollution_history_cars_ev15.csv', delimiter=',')
#ev_20 = np.genfromtxt(basedir + 'pollution_history_cars_ev20.csv', delimiter=',')
ev_59 = np.genfromtxt(basedir + 'pollution_history_cars_ev54.csv', delimiter=',')
trucks_baseline = np.genfromtxt(basedir + 'pollution_history_trucks_baseline.csv', delimiter=',')
trucks_ev_10 = np.genfromtxt(basedir + 'pollution_history_trucks_ev10.csv', delimiter=',')
trucks_ev_20 = np.genfromtxt(basedir + 'pollution_history_trucks_ev20.csv', delimiter=',')
time = np.arange(len(ev_59))

plt.plot(time, baseline, label='Cars Baseline')
plt.plot(time, trucks_baseline, label='Trucks baseline')
#plt.plot(time, ev_10, label='EV 10')
#plt.plot(time, ev_20, label='EV 20')
plt.plot(time, ev_59, label='Cars EV 54')
plt.plot(time, trucks_ev_10, label='Trucks EV 10')
plt.plot(time, trucks_ev_20, label='Trucks EV 20')
plt.xlabel("Timetep")
plt.ylabel("Total NOx")
plt.xlim([len(ev_59)/2, len(ev_59)])
plt.ylim([150, 400])
plt.title("Total NOx over time, no wind")
plt.legend()
plt.show()
#plt.savefig("./plots/cooling_schedule.png")
#plt.clf() #clear

values = [baseline[-1], trucks_baseline[-1], ev_59[-1], trucks_ev_10[-1], trucks_ev_20[-1]]
x_values = np.arange(len(values))
plt.bar(x_values, values)
plt.xlabel("Scenario")
plt.ylabel("Total NOx")
plt.ylim([250, 350])
plt.title("Total NOx at the end of each scenario, no wind")
plt.legend()
plt.show()
#plt.savefig("./plots/cooling_schedule.png")
#plt.clf() #clear

s_trucks_baseline = np.genfromtxt(basedir + 'pollution_sampled_trucks_baseline.csv', delimiter=',')
s_trucks_ev_10 = np.genfromtxt(basedir + 'pollution_sampled_trucks_ev10.csv', delimiter=',')
s_trucks_ev_20 = np.genfromtxt(basedir + 'pollution_sampled_trucks_ev20.csv', delimiter=',')
s_baseline = np.genfromtxt(basedir + 'pollution_sampled_cars_baseline.csv', delimiter=',')
s_ev54 = np.genfromtxt(basedir + 'pollution_sampled_cars_ev54.csv', delimiter=',')
time = np.arange(len(s_baseline))

plt.plot(time, s_baseline, label='Cars baseline')
plt.plot(time, s_ev54, label='Cars EV 54')
plt.plot(time, s_trucks_baseline, label='Trucks baseline')
plt.plot(time, s_trucks_ev_10, label='Trucks EV 10')
plt.plot(time, s_trucks_ev_20, label='Trucks EV 20')
plt.xlabel("Timetep")
plt.ylabel("Total NOx")
plt.title("Total NOx over time, no wind")
plt.legend()
plt.show()
#plt.savefig("./plots/cooling_schedule.png")
#plt.clf() #clear
