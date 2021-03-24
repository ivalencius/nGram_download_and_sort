# Extracts all links from http://storage.googleapis.com/books/ngrams/books/datasetsv2.html and saves to txt file
import re

filename = 'links_src.txt'
infile = open(filename,'r')
outfile = open('links.txt','w')
lines = infile.readlines()
#reg_exp = "^[http].*[.gz]$"
#links = re.findall(reg_exp, lines)
for line in lines:
    m = re.search('http(.+?).gz', line)
    if m:
        link = m.group(0)
        outfile.write(link)
        outfile.write('\n')

infile.close()
outfile.close()
