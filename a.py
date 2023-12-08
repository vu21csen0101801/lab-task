f = open("/b.txt", "r")

import matplotlib.pyplot as plt
import numpy as np
# hard code variables
def quadratic_model(f,time):
  a=float(f.readline())
  b=int(f.readline())
  c=int(f.readline())
  temperature = a*time*time + b*time + c
  return temperature

time_values=np.linspace(0,10,50)
temperature_hardcoded = quadratic_model(f,time_values)

plt.plot(time_values,temperature_hardcoded, label='temperature with hard coded coefficients')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.legend()
plt.title('weather modeling with quadratic equation(read from file)')
plt.show()
