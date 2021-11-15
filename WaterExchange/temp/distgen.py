#import glob
import os
linecounter = 1
waterid = 0
f = open("lifetime.dat", "r")
for line in f.readlines():
  if linecounter % 2 == 0:
    waterid = line[line.find("CA_1@CA-WAT_") + 12 : line.find("@O-H1")]
    print(waterid)
    os.system("echo 'distance DIST%s :CA :%s@O out dist%s.out' >> dist.in"%(waterid, waterid, waterid))
  linecounter += 1
f.close()

quit()
