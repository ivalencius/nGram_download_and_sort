# File to prep sorted ngrams for word2vec testing -> keep only text
import os
import gzip
import glob
import re
import time

from config import *

# Filenames for input and output of preprocessing
FILENAME_input = "1940_testing.gz"
FILENAME_output = "1940_testing.txt"

file_input = gzip.open(DIR_SORTED+FILENAME_input, 'r')
file_output = open("/home/ilanv/Documents/tmp/"+FILENAME_output, 'a')

for line in file_input:
    line = line.decode("utf-8") # data returned as bytes --> convert to string
    line_split = re.split(r'(\t)', line) # line now --> [ngram, \t ,year, \t , match_count, \t, volume_counts\n]
    file_output.writelines(line_split[0].lower()+"\n")

