import sys
import getopt
import os
import numpy
from pylab import *
from AnnoteFinder import *
from PymolLauncher import *
from pymol import *

#Prints how to use this script to the screen
def usage():
    print """Usage: %s
    Plot scatter file.

    -f : Rosetta results file
    -n : Native relax results file

    """ % sys.argv[0]
    sys.exit(-1)
try:
    opts, files = getopt.getopt(sys.argv[1:],"f:n:")
except getopt.GetoptError:
    usage()

#Declare input variables and store them from commandline to their containers

score_file = None
native_pdb = None

for opt, arg in opts:
    if opt == '-f':
        score_file = arg
    if opt == '-n':
        native_pdb = arg

# If parameters are missing when launching the script, print usage
if score_file is None:
    usage()
if native_pdb is None:
    usage()

# Your code here!
# Implement code that reads the score file and produces a energy vs. GDT_TS scatter plot. Don't forget to label the axis!












### Code that links the data to the PymolLauncher Object
### Uncomment this if you have edited this file and are ready
### to link the PymolLauncher to the scatter plot
#pl1 = PymolLauncher( gdt, scores, pdbs )
#pl1.set_native(native_pdb)
#connect('button_press_event', pl1)
#gca().set_autoscale_on(False)

#import __main__
#__main__.pymol_argv = [ 'pymol']

#import pymol

#pymol.finish_launching()

#from pymol import cmd
#show()
###/end Code that links the data to PymolLauncher


