import os
import gzip
import glob
import re
import time

from config import *

# Create timeline files
# Filetype can easily be changed pt1 --> switch ".gz" to whatever
ngramPre  = os.path.join(DIR_SORTED, 'pre_1899.gz')
ngram1900 = os.path.join(DIR_SORTED, '1900_1909.gz')
ngram1910 = os.path.join(DIR_SORTED, '1910_1919.gz')
ngram1920 = os.path.join(DIR_SORTED, '1920_1929.gz')
ngram1930 = os.path.join(DIR_SORTED, '1930_1939.gz')
ngram1940 = os.path.join(DIR_SORTED, '1940_1949.gz')
ngram1950 = os.path.join(DIR_SORTED, '1950_1959.gz')
ngram1960 = os.path.join(DIR_SORTED, '1960_1969.gz')
ngram1970 = os.path.join(DIR_SORTED, '1970_1979.gz')
ngram1980 = os.path.join(DIR_SORTED, '1980_1989.gz')
ngram1990 = os.path.join(DIR_SORTED, '1990_1989.gz')
ngram2000 = os.path.join(DIR_SORTED, '2000_2009.gz')

# Open timeline files
# Filetype can easily be changes pt2 --> delete "gzip." and change "wt" to "w"
filePre  = gzip.open(ngramPre, "wt")
file1900 = gzip.open(ngram1900, "wt")
file1910 = gzip.open(ngram1910, "wt")
file1920 = gzip.open(ngram1920, "wt")
file1930 = gzip.open(ngram1930, "wt")
file1940 = gzip.open(ngram1940, "wt")
file1950 = gzip.open(ngram1950, "wt")
file1960 = gzip.open(ngram1960, "wt")
file1970 = gzip.open(ngram1970, "wt")
file1980 = gzip.open(ngram1980, "wt")
file1990 = gzip.open(ngram1990, "wt")
file2000 = gzip.open(ngram2000, "wt")

## Layout of file
# ngram TAB year TAB match_count TAB volume_count NEWLINE
file_list = glob.glob(DIR_DATA+"*.gz")
file_num = len(file_list)
file_count = 1
total_gb = 0
time_fullStart = time.time()
for filename in file_list:
    t0 = time.time()
    print("Working on File: "+str(file_count))
    file_gb = os.path.getsize(filename)/1000000000
    total_gb += file_gb
    print("\tFile size = "+str(file_gb)+" GB")
    file_count += 1
    with gzip.open(filename, 'r') as f: # open in readonly mode
        for line in f:
            line = line.decode("utf-8") # data returned as bytes --> convert to string
            line_split = re.split(r'(\t)', line) # line now --> [ngram, \t ,year, \t , match_count, \t, volume_counts\n]
            # Change the following code to sort based on your needs
            year = int(line_split[2])
            if year >= 2000:
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
    t1 = time.time()
    print("\tComputation time: "+str(t1-t0))
    # Uncomment to delete file after parsing (storage considerations)            
    #os.remove(filename)
time_fullEnd = time.time()
print("\nFULL COMPUTATION TIME: "+str(time_fullEnd-time_fullStart))
print("TOTAL AMOUNT OF DATA PARSED: "+str(total_gb))