import sys
import numpy as np
import matplotlib.pyplot as plt

font = {'family' : 'normal',
        'weight' : 'bold',
        'size' : 20}
plt.rc('font', **font)

results = [['car_2.lus', '0.1', '0.2', '0.204'], ['car_1.lus', '0.104', '0.2', '0.203'],
  ['car_3.lus', '0.106', '0.205', '0.201'], ['car_3_e2_695.lus', '0.104', '0.203', '0.201']]

#with open("/home/dr41k/ownCloud/crisys/test/aeval/agacek/benchmarks/overhead_new.csv") as f:
#    results = [ line.strip().split(" ") for line in f if line.strip() != "" ]

#results.sort()

#pl0 = np.array([j[0] for j in sorted(results, key=lambda res: res[1])])
pl1 = np.array([float(j[1]) for j in sorted(results, key=lambda res: res[1])])
pl2 = np.array([float(j[2]) for j in sorted(results, key=lambda res: res[1])])
pl3 = np.array([float(j[3]) for j in sorted(results, key=lambda res: res[1])])


#print pl0
#print pl1
#print pl2
# f = open('results.csv','w')
# for i in sorted(results1), j in sorted(results2)
#     f.write()

# Plot the results
fig = plt.figure()

plt.yscale('log')
# plt.axis([0,1500,0,1500])
realizability = plt.plot(pl1,'-bs', label = 'JRealizability')
synthesis = plt.plot(pl2,'-r^', label = 'Synthesis')
fixpoint = plt.plot(pl3,'-g^', label = 'Fixpoint')

#plt.scatter(Yte, y, c="k", label="training samples")
#plt.scatter(Yte, y_1, c="g", label="max_depth=2")
#plt.scatter(Yte, y_2, c="r", label="max_depth=5")
plt.xlabel("Model")
plt.ylabel("Performance (seconds)")

plt.legend(bbox_to_anchor=(0.6, 1))

fig.savefig("overhead.pdf")
