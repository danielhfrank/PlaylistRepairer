#!/usr/bin/env python
'''
Takes in an iTunes-generated m3u file and creates a dir containing files, plus a new m3u with
relative pathnames so that it can all be sent to someone else
'''

import os
import sys
import shutil

rawk = '_+880______________________________\n_++88______________________________\n_++88______________________________\n__+880__________________________++_\n__+888_________________________+88_\n__++880________________________+88_\n__++888_______+++88__________++88__\n__+++8888__+++88880++888____+++88__\n___++888+++++8888+++888888+++888___\n___++88++++88888+++8888888++888____\n___+++++++88888888888888888888_____\n___++++++++88888888888888888888____\n___+++++++++0088888888888888888____\n____++++++++0088888888888888888____\n_____++++++++000888888888888888____\n_____+++++++++08888888888888888____\n______++++++++0888888888888888_____\n________+++++++88888888888888______\n________+++++++88888888888888______'


m3us = filter(lambda x: x.endswith(".m3u"),os.listdir("."))
if len(m3us) == 0:
	print("No M3Us in this dir!")
	sys.exit(1)
m3u = m3us[0]
print("using " + m3u)

f = open(m3u, 'r')
contents = f.readline()
f.close()

lines = contents.split("\r")#had to escape this one differently (more \) on ubuntu
absPaths = [x for x in lines if x.startswith("/")]

dr = m3u[:-4]
os.mkdir(dr)

#Copy all the songs into the dir - can be done in one call to cp
for songPath in absPaths:
	shutil.copy(songPath, dr)


#and now write them all to a file
f2 = open(dr + "/" + m3u, 'w')
f2.write("\r".join(['#EXTM3U'] + [x.split("/")[-1] for x in absPaths]))
f2.close()

print rawk

#finally, trash that original m3u file
os.system("rm -f " + m3u)
	
