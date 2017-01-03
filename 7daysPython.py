#! /usr/bin/env python
#coding=utf-8


import os
import glob
import sys
import shutil
import logging
import datetime
import time

from datetime import datetime
from datetime import date, timedelta

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

now = time.time()
cutoff = now - (7 * 86400)

print """
#####
Start Python Script to HouseKeep LOG Files inside "YourFolder"
#####"""


file=glob.glob("/home/loglib/loglib/*"); print '\n'.join(file)


logger = open("/home/loglib/HouseKeepLOGLIB_%s.txt"%datetime.now().strftime('%d%m%y'), "a")


for filename in file:
     if os.path.isfile(filename):
          t = os.stat(filename)
          c = t.st_mtime

          if  c < cutoff:
              os.remove(filename)
              logger.write('Deleted: %s (%s)' % (filename, cutoff) + '\n')
logger.close()
