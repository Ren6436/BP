import matplotlib.pyplot as plt
import matplotlib.cm as cm

from hypothesis.hypothesis import run_hypotheses
from hypothesis.hypothesis2 import run_hypotheses2
from questions import *

if __name__ == "__main__":
    run_hypotheses(plt, cm)
    run_hypotheses2(plt, cm)
