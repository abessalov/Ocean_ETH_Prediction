#%matplotlib inline
import seaborn as sns
import numpy as np
import pandas as pd
import re
import sys
import os
from matplotlib import pyplot as plt

from IPython.core.display import display, HTML
from IPython.display import IFrame
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
import warnings
warnings.filterwarnings('ignore')

plt.style.use('fivethirtyeight')
pd.set_option('display.max_columns',150)
pd.set_option('display.max_rows',500)
pd.options.display.float_format = '{:,.2f}'.format
display(HTML("<style>.container { width:80% !important; }</style>"))

import json
import pickle
from datetime import datetime as dt
from tqdm import tqdm
import gc
import itertools
from glob import glob
import shutil

from sklearn import metrics
from sklearn import preprocessing