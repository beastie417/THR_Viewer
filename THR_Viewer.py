import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from matplotlib.animation import FuncAnimation

root = tk.Tk()
root.withdraw()

while True:
    try:
        #Interactive file selection
        file_path = filedialog.askopenfilename()

        #THR files do not typically have headers
        columns = ["theta","rho"]
        reader = pd.read_csv(file_path, names=columns, delimiter=" ", header=None, comment='#')

        #Initialize plot and subplot
        fig = plt.figure()
        circle = fig.add_subplot(projection='polar')

        #Open plot window maximized
        figManager = plt.get_current_fig_manager()
        figManager.window.state('zoomed')

        #Configure how many frames the animation will have
        ticks = 100
        speedup = int(len(reader.theta)/ticks)


        def animate(i):
            circle.clear()
            # Plot that point using the x and y coordinates
            circle.plot(reader.theta[0:i*speedup], reader.rho[0:i*speedup], marker='none', linestyle='--')
            
            # Set the x and y axis to display a fixed range
            circle.set_xticks([])
            circle.set_yticks([])
            circle.set_ylim([0, 1])

            #Make increasing angle clockwise
            circle.set_theta_direction(-1)
        
            #Shift 0 deg to top of graph
            circle.set_theta_offset(np.pi/2.0)

        ani = FuncAnimation(fig, animate, frames=ticks+30, interval=10, repeat=True)


        # display the Polar plot
        plt.show()
    except:
        #User aborted file selection
        break

print("File selection aborted")