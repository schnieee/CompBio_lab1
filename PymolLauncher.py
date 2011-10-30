import math

import pylab
import matplotlib
from AnnoteFinder import *
import os
from pymol import cmd

"""
Inherents from AnnoteFinder
"""
class PymolLauncher(AnnoteFinder):
    def set_native(self, native):
        self.native = native
    """
    This is a derived class from AnnoteFinder!

    Overwritten draw annote, extended to start pymol and show predicted/native structures

    Edit this file! Implement a functionallity that shows the superimposed native structure and the prediction in pymol
    you can use PyMol commands you already know in python style ( cmd.your_command(arguments) ) to achieve this!

    Make sure that your structures are differently colored, in cartoon representation and zoomed in!

    """
    def drawAnnote(self, axis, x, y, annote):

        if (x,y) in self.drawnAnnotations:
            markers = self.drawnAnnotations[(x,y)]
            for m in markers:
                m.set_visible(not m.get_visible())
            self.axis.figure.canvas.draw()

        else:
           """
           Mark data point and show data
           """
           t = axis.text(x,y, "(%3.2f, %3.2f)"%(x,y), )
           m = axis.scatter([x],[y], marker='d', c='r', zorder=100)
           self.drawnAnnotations[(x,y)] =(t,m)
           self.axis.figure.canvas.draw()

           # Your code here!

           import os.path

           # Prepare names and paths
           structNative = os.path.basename(self.native).split(".")[0]
           structPredicted = annote
           pathNative = self.native
           pathPredicted = os.path.join(os.path.dirname(self.native), annote + ".pdb")

           import pymol

           # Load & arrange the native structure
           cmd.load(pathNative)
           cmd.do("hide everything, " + structNative)
           cmd.do("show cartoon, " + structNative)
           cmd.do("color white, " + structNative)

           # Load & arrange the predicted structure
           cmd.load(pathPredicted)
           cmd.do("hide everything, " + structPredicted)
           cmd.do("show cartoon, " + structPredicted)
           cmd.do("color yellow, " + structPredicted)

           # Allign the two sturctures
           cmd.do("align " + structPredicted + ", " + structNative)
           cmd.do("super " + structPredicted + ", " + structNative)
           cmd.do("zoom")

