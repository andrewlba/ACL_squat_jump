import pandas as pd
import matplotlib.pyplot as plt
from preProcess import jumpSquatPreProcess

filename = '../data/BFR007_squat_jump.csv'
data = pd.read_csv(filename, header=6)

#plt.rcParams['figure.figsize'] = [12,12]
#plt.rcParams.update({'font.size': 18})

processedData, BFR007index_pd, BFR007_weight = jumpSquatPreProcess(data)
print(BFR007_weight)

print(BFR007index_pd)

plt.plot(processedData['time'],processedData['ground_force_totaly'], color = 'k',label = 'Vertical Force')

plt.axvline(x = processedData['time'][BFR007index_pd['Jump 1 Start'][0]], color = 'b', label = 'Event Start')
plt.axvline(x = processedData['time'][BFR007index_pd['Jump 2 Start'][0]], color = 'b')
plt.axvline(x = processedData['time'][BFR007index_pd['Jump 3 Start'][0]], color = 'b')

plt.axvline(x = processedData['time'][BFR007index_pd['Jump 1 End'][0]], color = 'c', label = 'Event End')
plt.axvline(x = processedData['time'][BFR007index_pd['Jump 2 End'][0]], color = 'c')
plt.axvline(x = processedData['time'][BFR007index_pd['Jump 3 End'][0]], color = 'c')

plt.axvline(x = processedData['time'][BFR007index_pd['Jump 1 Start'][1]], color = 'g', label = 'Eccentric Start')
plt.axvline(x = processedData['time'][BFR007index_pd['Jump 2 Start'][1]], color = 'g')
plt.axvline(x = processedData['time'][BFR007index_pd['Jump 3 Start'][1]], color = 'g')

plt.axvline(x = processedData['time'][BFR007index_pd['Jump 1 Start'][2]], color = 'r', label = 'Concentric Start/Stop')
plt.axvline(x = processedData['time'][BFR007index_pd['Jump 1 End'][2]], color = 'r')
plt.axvline(x = processedData['time'][BFR007index_pd['Jump 2 Start'][2]], color = 'r')
plt.axvline(x = processedData['time'][BFR007index_pd['Jump 2 End'][2]], color = 'r')
plt.axvline(x = processedData['time'][BFR007index_pd['Jump 3 Start'][2]], color = 'r')
plt.axvline(x = processedData['time'][BFR007index_pd['Jump 3 End'][2]], color = 'r')


plt.axvline(x = processedData['time'][BFR007index_pd['Jump 1 Start'][4]], color = 'y', label = 'Landing Start')
plt.axvline(x = processedData['time'][BFR007index_pd['Jump 2 Start'][4]], color = 'y')
plt.axvline(x = processedData['time'][BFR007index_pd['Jump 3 Start'][4]], color = 'y')

plt.legend()
plt.show()   