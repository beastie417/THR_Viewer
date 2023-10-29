import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import tkinter as tk
import glob
import os
from tkinter import filedialog
from matplotlib.animation import FuncAnimation


root = tk.Tk()
root.withdraw()


#Interactive file selection
file_directory = filedialog.askdirectory()

file_list = glob.glob("*.thr",root_dir = file_directory)

#print(file_list)

if not os.path.exists(file_directory + "/GIFs"):
    os.makedirs(file_directory + "/GIFs")

for file_rel in file_list:

    file_path = file_directory + "/" + file_rel
    #THR files do not typically have headers
    columns = ["theta","rho"]
    reader = pd.read_csv(file_path, names=columns, delimiter=" ", header=None, comment='#')

    #Initialize plot and subplot
    fig = plt.figure()
    circle = fig.add_subplot(projection='polar')

    #Open plot window maximized
    #figManager = plt.get_current_fig_manager()
    #figManager.window.state('zoomed')

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

    ani = animation.FuncAnimation(fig, animate, frames=ticks+30, interval=10, repeat=True)

    #Save as GIF
    writer = animation.PillowWriter(fps=15,metadata=dict(artist='Me'),bitrate=1800)
    ani.save(file_directory + "/GIFs/" + file_rel.strip(".thr") + ".gif", writer = writer)

    plt.close('all')

    print(file_rel)

    # display the Polar plot
    #plt.show()
