#Brandon Marshall       
#Python Scripting
#October 1, 2015
#Homework 4 - File Traverser

import data_load
import indexer
import searcher

data_load.get_traversal_data()
indexer.process_data("raw_data.pickle", "fortunes_shelve", "indexed_files")
searcher.search("fortunes_shelve", "indexed_files")