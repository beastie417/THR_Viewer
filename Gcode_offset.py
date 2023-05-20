import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import re

root = tk.Tk()
root.withdraw()

while True:
    try:
        #Interactive file selection
        file_path = filedialog.askopenfilename()

        #THR files do not typically have headers
        columns = ["G","X","Y"]
        reader = pd.read_csv(file_path, names=columns, delimiter=" ", header=None, comment=';')

        reader.X = ["X{:.3f}".format(float(coordinate.strip("X"))-200) for coordinate in reader.X]
        reader.Y = ["Y{:.3f}".format(float(coordinate.strip("Y"))-200) for coordinate in reader.Y]

#        print(reader.X)

        reader.to_csv("output.gcode", sep = " ", index = False, header = None)


    except:
        #User aborted file selection
        break

print("File selection aborted")