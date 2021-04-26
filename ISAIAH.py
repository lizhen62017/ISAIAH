# coding=utf-8
#import xlrd
import numpy as np
from matplotlib import cm
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.ticker as ticker
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import statistics

# copied for plotting diffusion coefficient

# workbook = xlrd.open_workbook('Research.xlsx')
# seventh_sheet = workbook.sheet_by_index(6)

f1 = open('input.in', 'r')
setnum = len(f1.readlines())
f1.close()

raw = [[] for j in range(8*setnum)]
xval = [0.323,0.25,0.202,0.162]
yval = []
ydev = []
markers = ['o','^', 's']
sets = ['126-HFE', '126-IOD', '12-6-4']

f2 = open('test.out', 'r') 
Lines = f2.readlines()
runs = 0
for line in Lines[1:]:
  if line.strip():
    if line[0] != 'f': 
      if float(line) <= 3.0 and float(line) >= 0.3: 
        raw[runs].append(float(line))
  else:
    runs += 1
f2.close()

for s in range(int(setnum/3)):
  for r in range(12): 
    ydev.append(statistics.stdev(raw[24*s+r*2]))
    yval.append(statistics.mean(raw[24*s+r*2])/statistics.mean(raw[24*s+r*2+1])*2.3)
  for i in range(3):            
    plt.errorbar([x+0.003*((i+2)%3) for x in xval], yval[4*s+4*i:4*s+4+4*i], yerr=ydev[4*s+4*i:4*s+4+4*i], marker=markers[i], fmt='o',capsize=5)
    a,b=np.polyfit(xval, yval[4*s+4*i:4*s+4+4*i], 1)
    poly1d_fn = np.poly1d((a,b))
    plt.plot([x+0.003*((i+2)%3) for x in xval], poly1d_fn(xval),'--', color='C'+str(i))
    plt.text(0.27, 0.69-0.07*((i+2)%3), sets[i], color='C'+str(i))
    plt.text(0.27, 0.67-0.07*((i+2)%3), 'y='+str(round(a,3))+'x+'+str(round(b,3)), color='C'+str(i))
  plt.ylabel("Diffusion Coefficient (10$^{-5}$cm$^{2}$/s)", fontsize=10)
  plt.xlabel("1/(Water box lengths) (nm$^{-1}$)", fontsize=10)

  f1 = open('input.in', 'r')
  line = f1.readlines()[s*3]
  plt.savefig('%s_%s.png'%(line.split()[0], line.split()[1]))
  plt.close()
  f1.close()

# previous one for plotting PMF
"""
plot_txt=[]
argv_len=len(sys.argv)-1
#argv=sys.argv.split()
for num in range(1,argv_len):
  txt_path=sys.argv[num]
  #print (txt_path)
  lable,txt_name=txt_path.rsplit("/", 1)
  #print(lable)
  #print(txt_name)
  os.system("cp %s %s-%s"%(txt_path,lable,txt_name))

  f2=open("%s-%s-plot.txt"%(lable,txt_name),"w")
  with open("%s"%(txt_path)) as f1:
    for line in (f1.readlines()[1:901]):
      #print (line)
      a,b,c,d,e=line.split()
      f2.write("%s	%s\n"%(a,b))
  f1.close()
  f2.close()

  #plottxt_name=lable+txt_name+'-plot.txt'
  plot_txt.append("%s-%s-plot.txt"%(lable,txt_name))

def dis_energ(fil_name):
  distance=[]
  energy=[]
  with open("%s"%(fil_name)) as f2:
    for line in (f2.readlines()[0:900]):
      #print (line)
      a,b=line.split()
      distance.append(a)                          
      energy.append(b)
  f2.close()                                    
  distance_f=[float(i) for i in distance]
  energy_f=[float(j) for j in energy]
  label,rest=fil_name.split('-2.')
  return distance_f, energy_f,label

#print (plot_txt)

font = {"fontname":"Helvetica"}
colors = ['red', 'orange', 'green', 'blue','black','magenta','cyan','yellow','brown','grey']
fig, axe = plt.subplots()
num_curve=len(plot_txt)
for num_c in range(num_curve):
  dis,ene,lab=dis_energ(plot_txt[num_c])
  axe.plot(dis,ene,label = lab, linestyle = '-', linewidth = 1, color = colors[num_c])
#axe.text(6, 13, names[0], fontsize=15)
axe.set_xlabel("r$_{M-C}$ (A)",fontsize=10)
axe.set_ylabel("delta G (kcal/mol)",fontsize=10)
for m in axe.xaxis.get_major_ticks():
    m.label.set_fontsize(10)
for n in axe.yaxis.get_major_ticks():
    n.label.set_fontsize(10)
axe.legend(loc = 1, prop = {'size': 7})
plt.savefig('%s.png'%(sys.argv[-1]))


def cal_energy(fil_name):
  bind_ene=1000
  with open("%s"%(fil_name)) as f2:
    for line in (f2.readlines()[899:900]):
      a,b=line.split()
      end_dis=float(a)
      end_ene=float(b)
  f2.close()
  with open("%s"%(fil_name)) as f2:
    for line in (f2.readlines()[0:900]):
      #print (line)
      a,b=line.split()
      if float(a) < 4.5:
        if float(b) < bind_ene:
           bind_ene=float(b)
           bind_dis=float(a)
      else:
        break
  f2.close()
  binding_free_energy=round((-end_ene+bind_ene),2)
  label,rest=fil_name.split('-2.')
  return label,end_dis,end_ene,bind_dis,bind_ene,binding_free_energy

f3=open("result.txt","a")
for num_c in range(num_curve):
  labe,end_dist,end_ener,bind_dist,bind_ener,binding_free_energ=cal_energy(plot_txt[num_c])
  print ("%s %s	%s %s %s %s"%(labe,end_dist,end_ener,bind_dist,bind_ener,binding_free_energ))
  f3.write("%s %s %s %s %s %s\n"%(labe,end_dist,end_ener,bind_dist,bind_ener,binding_free_energ))
"""
