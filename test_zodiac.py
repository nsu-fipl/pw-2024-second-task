from matplotlib.testing.decorators import image_comparison
import matplotlib.pyplot as plt
import numpy as np

@image_comparison(baseline_images=['plot'], remove_text=True,
                  extensions=['png'], style='fivethirtyeight')
def test_plot():
    # TODO: insert your code here
    pass

@image_comparison(baseline_images=['bar'], remove_text=True,
                  extensions=['png'], style='fivethirtyeight')
def test_bar():
    # TODO: insert your code here
    pass

@image_comparison(baseline_images=['hist'], remove_text=True,
                  extensions=['png'], style='fivethirtyeight')
def test_hist():
    # TODO: insert your code here
    pass