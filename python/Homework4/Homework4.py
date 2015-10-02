#Brandon Marshall       
#Python Scripting
#September 28, 2015
#Homework 4 - File Traverser

import searcher
import data_load
import indexer

d = indexer.process_data("raw_data.pickle", "fortunes_shelve", "indexed_files")
searcher.search("fortunes_shelve", "indexed_files")