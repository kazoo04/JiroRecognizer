#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re
import numpy as np
import scipy.cluster
from pylab import *
import random

def getVectors(path):
  vectors = []
  files = os.listdir(path)

  for f in files:
    m = re.match(r'.+\.sift', f, re.IGNORECASE)
    if m:
      fileObj = open(path + '/' + f, 'r')
      while True:
        line = fileObj.readline()
        if not line:
          break
        if random.random() < 0.1:
          try:
            vectors.append([float(i.strip()) for i in line.split(',')])
          except:
            continue

  return vectors

if __name__ == "__main__":
  vectors = []
  directory = 'sift/negative'

  vectors += getVectors('sift/positive')

  vectors += getVectors('sift/negative')

  X= np.array(vectors)

  codebook, destortion = scipy.cluster.vq.kmeans2(X, 1024, iter=16, thresh=1e-03)
  for row in codebook:
    print ','.join([str(r) for r in row])

