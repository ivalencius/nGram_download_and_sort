import os
import gzip
import glob
import re

from config import *

# Create timeline files
# Filetype can easily be changed pt1 --> switch ".gz" to whatever
namePre = os.path.join(DIR_SORTED, 'pre_1899.gz')
name1900 = os.path.join(DIR_SORTED, '1900_1909.gz')
name1910 = os.path.join(DIR_SORTED, '1910_1919.gz')
name1920 = os.path.join(DIR_SORTED, '1920_1929.gz')
name1930 = os.path.join(DIR_SORTED, '1930_1939.gz')
name1940 = os.path.join(DIR_SORTED, '1940_1949.gz')
name1950 = os.path.join(DIR_SORTED, '1950_1959.gz')
name1960 = os.path.join(DIR_SORTED, '1960_1969.gz')
name1970 = os.path.join(DIR_SORTED, '1970_1979.gz')
name1980 = os.path.join(DIR_SORTED, '1980_1989.gz')
name1990 = os.path.join(DIR_SORTED, '1990_1989.gz')
name2000 = os.path.join(DIR_SORTED, '2000_2009.gz')
name2010 = os.path.join(DIR_SORTED, '2010_2019.gz')

# Open timeline files
# Filetype can easily be changes pt2 --> delete "gzip." and change "wt" to "w"
filePre= gzip.open(namePre, "wt")
file1900 = gzip.open(name1900, "wt")
file1910 = gzip.open(name1910, "wt")
file1920 = gzip.open(name1920, "wt")
file1930 = gzip.open(name1930, "wt")
file1940 = gzip.open(name1940, "wt")
file1950 = gzip.open(name1950, "wt")
file1960 = gzip.open(name1960, "wt")
file1970 = gzip.open(name1970, "wt")
file1980 = gzip.open(name1980, "wt")
file1990 = gzip.open(name1990, "wt")
file2000 = gzip.open(name2000, "wt")
file2010 = gzip.open(name2010, "wt")

## Layout of file
# ngram TAB year TAB match_count TAB volume_count NEWLINE
file_list = glob.glob(DIR_DATA+"*.gz")
file_num = len(file_list)
file_count = 1
for filename in file_list:
    print("Working on File: "+str(file_count))
    print("\tFile size = "+str(os.path.getsize(filename))+" bytes")
    file_count += 1
    with gzip.open(filename, 'r') as f: # open in readonly mode
        for line in f:
            line = line.decode("utf-8") # data returned as bytes --> convert to string
            line_split = re.split(r'(\t)', line) # line now --> [ngram, \t ,year, \t , match_count, \t, volume_counts\n]
            # Change the following code to sort based on your needs
            year = int(line_split[2])
            if year >= 2010:
                file2010.writelines(line_split)
            elif year >= 2000:
                file2000.writelines(line_split)
            elif year >= 1990:
                file1990.writelines(line_split)
            elif year >= 1980:
                file1980.writelines(line_split)
            elif year >= 1970:
                file1970.writelines(line_split)
            elif year >= 1960:
                file1960.writelines(line_split)
            elif year >= 1950:
                file1950.writelines(line_split)
            elif year >= 1940:
                file1940.writelines(line_split)
            elif year >= 1930:
                file1930.writelines(line_split)
            elif year >= 1920:
                file1920.writelines(line_split)
            elif year >= 1910:
                file1910.writelines(line_split)
            elif year >= 1900:
                file1900.writelines(line_split)
            else:
                filePre.writelines(line_split)