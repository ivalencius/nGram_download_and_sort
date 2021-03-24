import os
import sys

home_path = os.getcwd()
DIR_ROOT = os.path.dirname(os.path.abspath(__file__))
# Change when not testing
DIR_DATA = os.path.join(DIR_ROOT, 'test_data/')
DIR_SORTED = os.path.join(DIR_ROOT, 'sorted_nGrams/')

