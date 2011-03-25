#!/usr/bin/env python
'''
Takes in an iTunes-generated m3u file and creates a dir containing files, plus a new m3u with
relative pathnames so that it can all be sent to someone else
'''

import os
import sys

def escape(x):
	tmp = x.replace("\n", "")
	tmp = tmp.replace("\r", "")
	tmp = tmp.replace(" ", "\ ")
	tmp = tmp.replace("&", "\&")
	tmp = tmp.replace(",", "\,")
	tmp = tmp.replace("\'", "\\\'")#had to escape this one differently (fewer \) on ubuntu
	tmp = tmp.replace("\"", "\\\"")
	tmp = tmp.replace("(", "\(")
	tmp = tmp.replace(")", "\)")
	return tmp

m3us = filter(lambda x: x.endswith(".m3u"),os.listdir("."))
if len(m3us) == 0:
	print("No M3Us in this dir!")
	sys.exit(1)
m3u = m3us[0]
print("using " + m3u)

f = open(m3u, 'r')
contents = f.readline()
f.close()

#print contents
lines = contents.split("\r")#had to escape this one differently (more \) on ubuntu
for line in lines:
#	print ">>>" + line
absPaths = [x for x in lines if x.startswith("/")]
escapedPaths = [escape(x) for x in absPaths]

#Make a dir for all this good stuff
dr = escape(m3u[:-4])
os.system("mkdir " + dr)

#Copy all the songs into the dir - can be done in one call to cp
call = "cp " + " ".join(escapedPaths) +  " " + dr
print call
os.system(call.strip())

#and now write them all to a file
f2 = open(dr + "/" + m3u, 'w')
f2.write("\r".join(['#EXTM3U'] + [x.split("/")[-1] for x in absPaths]))
f2.close()

#finally, trash that original m3u file
os.system("rm -f " + m3u)
	
