# Code for downloading and sorting Google nGram data based on year


## 1 Downloading Data

Data is downloaded from the [Google nGram Download Page](http://storage.googleapis.com/books/ngrams/books/datasetsv2.html)

1) Use inspect element (F11) to inspect and copy the html code containing the links for the nGrams you wish to download. Copy this code to "links_src.txt" (Example html for all 5-gram download links is included in this repo)
2) Run link_extraction.py. This will save all the extracted download links to "links.txt".
3) Copy/move links.txt to /data and run
    
    xargs -n 1 curl -O < links.txt

    
    in the linux terminal inside /data. This will download the data from every link sequentially.

## 2 Sorting the Data

1) Run nGram_sort.py. This will extract and sort all the nGrams in /data by year. Currently, the datatset will sort into buckets spanning pre1900, then ever 10 years till 2019. 
2) Data can be found in /sorted_nGrams

## Notes

1) This data takes up **a lot** (all 5Grams with sorted data $$\approx$$ of space and will take a fair bit of time to run so plan accordingly.
2) Currently the data is sorted by year - this can easily be changed in nGram_sort.py (see comment).
3) The code is currently stored in .gz files to save space. This is totally optional and the file type can easily be changed in nGram_sort.py (see comments).