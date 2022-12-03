import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# the chemical shifts
shift = []

# the intensities
intensities = []

## Put the name of the file in the quotes
##in the line immediately below:
with open('','r') as inf:
    for line in inf:
        line = line.strip().split(',')
        shift.append(float(line[0]))
        intensities.append(float(line[1]))

shift = np.asarray(shift)
intensities = np.asarray(intensities)

# Let's plot the spectrum
plt.plot(shift,intensities,marker='')

# We need to invert the x axis so that our plot
# looks like a typical NMR spectrum, with increasing
# chemical shift to the left
plt.gca().invert_xaxis()

# Save it, if you want (give it a better name)
plt.savefig('nmrplot.pdf') 
