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

num_of_pages = 8

for start in range(100):

	connection = urllib2.urlopen('http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=%s&rsz=%d&start=%d' % (q, num_of_pages, start * num_of_pages))

	data = json.load(connection)
	connection.close()
	 
	results = data['responseData']['results']

	print data

	for result in results:
		url = result['url']

		m = re.match(r'.+\.(jpg|png)$', url, re.IGNORECASE)

		print
		print url

		if m:
			filename = hashlib.sha1(url).hexdigest() + '.' + m.group(1).lower()
			print filename

			try:
				urllib.urlretrieve(url, dist_dir + '/' + filename)
			except IOError:
				next

		 
