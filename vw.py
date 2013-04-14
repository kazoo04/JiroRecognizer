#!/usr/bin/env python
#coding: utf-8
 
import os
import sys
import re
import subprocess
 
if len(sys.argv) <= 2:
  print('Usage:')
  print('python vw.py centroids_file src_directory dist_directory')
  #exit()

codebook = []
codebook_file = open(sys.argv[1], 'r')
while True:
  line = codebook_file.readline()
  if not line:
    break
  
  codebook.append([float(i.strip()) for i in line.split(',')])

print codebook

#files = os.listdir(sys.argv[2])
