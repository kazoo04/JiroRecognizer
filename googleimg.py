#!/usr/bin/env python
#coding: utf-8
 
# Download a random picture from Google image search.
#
# Usage:
# $ fetch_google_image.py cat cute   # Download a cute cat picture
 
import os
import sys
import urllib
import urllib2
import json
import imghdr
import hashlib
import re
 
if len(sys.argv) <= 2:
  print('Usage:')
  print('python googleimg.py path query')
  exit()
 
dist_dir = sys.argv[1]
q = urllib.quote(sys.argv[2])

f = urllib2.urlopen('http://ajax.googleapis.com/ajax/services/search/images?q=' + q + '&v=1.0&rsz=8&start=1')
data = json.load(f)
f.close()
 
results = data['responseData']['results']

for result in results:
	url = result['url']

	m = re.match(r'.+\.(jpg|png)$', url, re.IGNORECASE)

	print
	print url

	if m:
		filename = hashlib.sha1(url).hexdigest() + '.' + m.group(1).lower()
		print filename

	urllib.urlretrieve(url, dist_dir + '/' + filename)
	 
