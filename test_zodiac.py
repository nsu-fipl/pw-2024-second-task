from matplotlib.testing.decorators import image_comparison
import matplotlib.pyplot as plt
import numpy as np


@image_comparison(baseline_images=['plot'], remove_text=False,
                  extensions=['png'])
def test_plot():
    # TODO: your code
    pass

@image_comparison(baseline_images=['bar'], remove_text=False,
                  extensions=['png'])
def test_bar():
    # TODO: your code
    pass

@image_comparison(baseline_images=['hist'], remove_text=False,
                  extensions=['png'])
def test_hist():
    # TODO: your code
    pass
