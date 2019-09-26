import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0, 10.0, 0.01)
y = 3.0* x + 1.0

noise = np.random.normal(0.0, 1.0, len(x))
plt.plot(x, y + noise, 'r.', label="Actual")
plt.plot(x, y, 'b-', label="Model")
plt.title("Simple plot")
plt.ylabel('Y Axis')
plt.xlabel('X Axis')
plt.legend() # legend needs to be added to variables
plt.grid()
plt.show()

#Example
#plt.plot([1, 2, 3, 4],[1, 4, 9, 16],'b*')
#plt.ylabel('some Y numbers')
#plt.xlabel('some X numbers')
#plt.show()