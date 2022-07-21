import os
from fink_science import __file__

curdir = os.path.dirname(os.path.abspath(__file__))
CLASSIFIER = curdir + "/data/AGN_binary.pkl"
MINIMUM_POINTS = 4
