import os
import gzip
import glob
import re

from alive_progress import alive_bar
from config import *

# Create timeline files
# Filetype can easily be changed pt1 --> switch ".txt" to whatever
ngramPre  = os.path.join(DIR_SORTED, 'pre_1899.txt')
ngram1900 = os.path.join(DIR_SORTED, '1900_1909.txt')
ngram1910 = os.path.join(DIR_SORTED, '1910_1919.txt')
ngram1920 = os.path.join(DIR_SORTED, '1920_1929.txt')
ngram1930 = os.path.join(DIR_SORTED, '1930_1939.txt')
ngram1940 = os.path.join(DIR_SORTED, '1940_1949.txt')
ngram1950 = os.path.join(DIR_SORTED, '1950_1959.txt')
ngram1960 = os.path.join(DIR_SORTED, '1960_1969.txt')
ngram1970 = os.path.join(DIR_SORTED, '1970_1979.txt')
ngram1980 = os.path.join(DIR_SORTED, '1980_1989.txt')
ngram1990 = os.path.join(DIR_SORTED, '1990_1989.txt')
ngram2000 = os.path.join(DIR_SORTED, '2000_2009.txt')

# Open timeline files
# Filetype can easily be changed to gzip -> add gzip.open and a -> at
filePre  = open(ngramPre, "a")
file1900 = open(ngram1900, "a")
file1910 = open(ngram1910, "a")
file1920 = open(ngram1920, "a")
file1930 = open(ngram1930, "a")
file1940 = open(ngram1940, "a")
file1950 = open(ngram1950, "a")
file1960 = open(ngram1960, "a")
file1970 = open(ngram1970, "a")
file1980 = open(ngram1980, "a")
file1990 = open(ngram1990, "a")
file2000 = open(ngram2000, "a")

## Layout of file
# ngram TAB year TAB match_count TAB volume_count NEWLINE
file_list = glob.glob(DIR_DATA+"*.gz")
with alive_bar(len(file_list)) as bar:
    for filename in file_list:
        with gzip.open(filename, 'r') as f: # open in readonly mode
            for line in f:
                line = line.decode("utf-8")
                line_split = re.split(r'(\t)',line)
                # line now --> [ngram, \t ,year, \t , match_count, \t, volume_counts\n]
                # Change the following code to sort based on your needs
                year = int(line_split[2])
                if year >= 2000:
                    file2000.writelines(line_split[0].lower()+"\n")
                elif year >= 1990:
                   file1990.writelines(line_split[0].lower()+"\n")
                elif year >= 1980:
                    file1980.writelines(line_split[0].lower()+"\n")
                elif year >= 1970:
                    file1970.writelines(line_split[0].lower()+"\n")
                elif year >= 1960:
                    file1960.writelines(line_split[0].lower()+"\n")
                elif year >= 1950:
                   file1950.writelines(line_split[0].lower()+"\n")
                elif year >= 1940:
                   file1940.writelines(line_split[0].lower()+"\n")
                elif year >= 1930:
                  file1930.writelines(line_split[0].lower()+"\n")
                elif year >= 1920:
                    file1920.writelines(line_split[0].lower()+"\n")
                elif year >= 1910:
                   file1910.writelines(line_split[0].lower()+"\n")
                elif year >= 1900:
                  file1900.writelines(line_split[0].lower()+"\n")
                else:
                  filePre.writelines(line_split[0].lower()+"\n")
        bar() 
    # Uncomment to delete file after parsing (storage considerations)            
    os.remove(filename)
