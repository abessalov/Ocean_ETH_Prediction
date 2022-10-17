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
pd.set_option('max_columns',150)
pd.set_option('max_rows',500)
pd.options.display.float_format = '{:,.2f}'.format
display(HTML("<style>.container { width:80% !important; }</style>"))
from collections import OrderedDict
from pandas import ExcelWriter

import json
import pickle
from datetime import datetime as dt
from tqdm import tqdm
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import gc
import itertools
from glob import glob
import shutil
from matplotlib_venn import venn2
from pivottablejs import pivot_ui
from dateutil.relativedelta import relativedelta
import sweetviz

from sklearn import metrics
from sklearn import feature_selection
from sklearn import preprocessing