#!/usr/bin/env python
#coding: utf-8
 
import os
import sys
import re
import subprocess
 
if len(sys.argv) <= 2:
  print('Usage:')
  print('python sift.py input_directory output_directory')
  exit()
 
files = os.listdir(sys.argv[1])

for f in files:
  m = re.match(r'(.+)\.(jpg|png)', f, re.IGNORECASE)
  if m:
    cmd = './sampling ' + sys.argv[1]  + '/' + f + ' -> ' + sys.argv[2] + '/' + m.group(1) + '.sift'
    print cmd
    sys.stdout.flush()
    subprocess.call(cmd, shell=True)

