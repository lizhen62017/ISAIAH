#import glob
import os
total = 0
waterperframe = {}
for frame in range(1,8001):
  waterperframe[frame]=[]
  f1 = open("lifetime.dat", "r")
  linecounter = 1
  waterid = 0
  for line1 in f1.readlines():
    if linecounter % 2 == 0:
      waterid = line1[line1.find("CA_1@CA-WAT_") + 12 : line1.find("@O-H1")]
      f2 = open("dist%s.out"%waterid, "r")
      for line2 in f2.readlines()[1:]:
        parts = line2.split()
        if float(parts[1]) <= UPUPUP and int(parts[0]) == frame:
          #print(waterid)
          #print(line2)
          waterperframe[frame].append([waterid, float(parts[1])])
      f2.close()
    linecounter += 1
  f1.close()
  print(waterperframe[frame])
  if frame > 2:
    for oldid in waterperframe[frame-2]: 
      # -2 in the list, no matter higher or lower than LOWLOW
      if oldid[0] not in [w[0] for w in waterperframe[frame-1]] \
	and oldid[0] not in [x[0] for x in waterperframe[frame]]:
	# both -1 and 0 should be out of list, i.e. larger than UPUPUP
        print("one deletion")
        total += 1
    for newid in waterperframe[frame]:
      if newid[1] <= LOWLOW \ # 0 needs to be lower than LOWLOW
	and newid[0] in [z[0] for z in waterperframe[frame-1]]:
	  # -1 needs to be in the list and lower than LOWLOW
	  if [a[1] for a in waterperframe[frame-1]][[b[0] for b in waterperframe[frame-1]].index(newid[0])] <= LOWLOW: 
	    # -2 should be out of list. Or if in list, higher than LOWLOW
	    if newid[0] not in [y[0] for y in waterperframe[frame-2]]: 
              print("one insertion")
              total += 1
            elif [c[1] for c in waterperframe[frame-2]][[d[0] for d in waterperframe[frame-2]].index(newid[0])] >= LOWLOW:
	      print("one insertion")
              total += 1
print(total)
quit()
