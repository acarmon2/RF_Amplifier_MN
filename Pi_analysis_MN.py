from matplotlib import pyplot as plt
import skrf as rf
from skrf import Network
from pysmithchart import S_PARAMETER

# Data from LibreVNA
PiNetWork1 = Network('MN_Pi_2R7pF_3R3nH_10R0pF.s2p')
PiNetWork2 = Network('MN_Pi_2R7pF_3R3nH_24R0pF.s2p')
PiNetWork3 = Network('MN_Pi_2R7pF_3R3nH_6R8pF.s2p')

# Extract the S11 parameter
S11_Pi1 = PiNetWork1['0.800-1.0 GHz'].s11
S11_Pi2 = PiNetWork2['0.800-1.0 GHz'].s11
S11_Pi3 = PiNetWork3['0.800-1.0 GHz'].s11

# Create the object to plot
fig, ax = plt.subplots(1, 1, figsize=(7, 8))
rf.plotting.smith(ax=ax, draw_labels=True, ref_imm=50.0, chart_type='z')

# Select 900MHz to put a marker in each plot
marker_index = 100
x_val = S11_Pi1.frequency.f_scaled[marker_index]
y_val = S11_Pi1.s_db[marker_index, 0, 0]
x_val
y_val

S11_Pi1.plot_s_smith(m=0, n=0, ax=ax, label='10 pF')
S11_Pi2.plot_s_smith(m=0, n=0, ax=ax, label='24 pF')
S11_Pi3.plot_s_smith(m=0, n=0, ax=ax, label='6.8 pF')

ax.scatter(x_val, y_val, marker='o', color='red', s=50, zorder=5)

ax.legend()
plt.show()