import os
import unittest

import numpy as np
import pandas as pd

import base
from base import jumpSquatPreProcess

data_path = os.path.join(base.__path__[0], 'data')
df = pd.read_csv(os.path.join(data_path, 'test.csv'),header = 6)


class TestpreProcess(unittest.TestCase):

    def test_smoke(self):
        '''
        Makes sure preProcess runs
        '''
        jumpSquatPreProcess(df)
        return



