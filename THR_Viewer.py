import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

columns = ["theta","rho"]

reader = pd.read_csv(file_path, names=columns, delimiter=" ", header=None, comment='#')
  
fig = plt.figure()

circle = fig.add_subplot(projection='polar')

circle.set_theta_direction(-1)

circle.set_theta_offset(np.pi/2.0)

circle.plot(reader.theta, reader.rho, marker='none', linestyle='--')

circle.set_xticks([])
circle.set_yticks([])

# display the Polar plot
plt.show()