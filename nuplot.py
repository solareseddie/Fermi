import numpy as np
import matplotlib.pyplot as plt
import sys

print """

	Light Curve Plot Generator v1.0!

	0 = Light Curve 
	1 = Energy Light Curve
	2 = Index Curve
	3 = Test Statistic Curve

"""


choice = input("Please choose which type of plot you want:")

tavg = list()
flux = list()
errflux = list()
errtime = list()
ts = list()
ul = list()
conv = list()
pl1flux = list()
pl2flux = list()
pl3flux = list()
pl1time = list()
pl2time = list()
pl3time = list()
pl1terr = list()
pl2terr = list()
pl3terr = list()
pl3flux = list()
pl3fluxerr = list()

if choice == 0:
  file_name = raw_input('Please enter lightcurve.txt file directory: ')
  file_title = raw_input('Enter title:')
  t_measure = raw_input('MET or MJD:')
  f_type = raw_input('Type PL2 for flux from the xml, else just press enter:')

  f = open(file_name,'r')    
  g = f.readlines()
  f1 = 6
  ef1 = 7
  if f_type == "PL2":
    f1 == 4
    ef1 == 5
    print 'PL2 will be used'


  for i in range(0, len(g)):
    if t_measure == 'MET':
      tavg.append((float(g[i].split()[0])+float(g[i].split()[1]))/2)
      errtime.append((float(g[i].split()[1])-float(g[i].split()[0]))/2)
    elif t_measure == 'MJD':
      tavg.append((float(g[i].split()[2])+float(g[i].split()[3]))/2)
      errtime.append((float(g[i].split()[3])-float(g[i].split()[2]))/2)
    else:
      print('Not a valid choice, MET or MJD.')
      sys.exit()
    flux.append(float(g[i].split()[f1]))
    errflux.append(float(g[i].split()[ef1]))
    ts.append(float(g[i].split()[12]))
    conv.append(float(g[i].split()[13]))
    ul.append(float(g[i].split()[15]))
    if conv[i] != 0:
      pl1flux.append(float(flux[i]))
      pl1time.append(float(tavg[i]))
    elif ts[i] < 10 or errflux[i]/flux[i] > 0.5:
      pl2flux.append(float(ul[i]))
      pl2time.append(float(tavg[i]))
      pl2terr.append(float(errtime[i]))
    else:
      pl3flux.append(float(flux[i]))
      pl3fluxerr.append(float(errflux[i]))
      pl3time.append(float(tavg[i]))
      pl3terr.append(float(errtime[i]))

  try:
      plt.plot(pl1time, pl1flux, marker='x', color='r', ls='none')
  except:
      print 'All points succesfully converged!'
  try:
      plt.errorbar(pl2time, pl2flux, xerr=pl2terr, marker='2', color='b', ls='none')
  except:
      print 'No upper limits found!'
  try:
      plt.errorbar(pl3time, pl3flux, xerr=pl3terr,yerr=pl3fluxerr, marker='o', color='g', ls='none')
  except:
      print 'Warning: No regular flux points detected, try re-running the light curve generator with a bigger bin interval.'
      print 'Recommended maximum bins is TS_{DC}/25.'
  plt.xlabel("Time in "+t_measure)
  plt.ylabel("Flux >0.1 GeV (ph cm^-2 s^-1)")
  plt.title(file_title)
  plt.axis
  plt.show()
elif choice == 1:
  file_name = raw_input('Please enter lightcurve.txt file directory: ')
  file_title = raw_input('Enter title:')
  t_measure = raw_input('MET or MJD:')

  f = open(file_name,'r')    
  g = f.readlines()

  for i in range(0, len(g)):
    if t_measure == 'MET':
      tavg.append((float(g[i].split()[0])+float(g[i].split()[1]))/2)
      errtime.append((float(g[i].split()[1])-float(g[i].split()[0]))/2)
    elif t_measure == 'MJD':
      tavg.append((float(g[i].split()[2])+float(g[i].split()[3]))/2)
      errtime.append((float(g[i].split()[3])-float(g[i].split()[2]))/2)
    else:
      print('Not a valid choice, MET or MJD.')
      sys.exit()
    flux.append(float(g[i].split()[8]))
    errflux.append(float(g[i].split()[9]))
    conv.append(float(g[i].split()[13]))
    if conv[i] != 0:
      pl1flux.append(float(flux[i]))
      pl1time.append(float(tavg[i]))
    else:
      pl3flux.append(float(flux[i]))
      pl3fluxerr.append(float(errflux[i]))
      pl3time.append(float(tavg[i]))
      pl3terr.append(float(errtime[i]))

  try:
      plt.plot(pl1time, pl1flux, marker='x', color='r', ls='none')
  except:
      print 'All points succesfully converged!'
  plt.errorbar(pl3time, pl3flux, xerr=pl3terr,yerr=pl3fluxerr, marker='o', color='g', ls='none')
  plt.xlabel("Time in "+t_measure)
  plt.ylabel("Energy Flux >0.1 GeV (MeV cm^-2 s^-1)")
  plt.title(file_title)
  plt.axis
  plt.show()
elif choice == 2:
  file_name = raw_input('Please enter lightcurve.txt file directory: ')
  file_title = raw_input('Enter title:')
  t_measure = raw_input('MET or MJD:')

  f = open(file_name,'r')    
  g = f.readlines()

  for i in range(0, len(g)):
    if t_measure == 'MET':
      tavg.append((float(g[i].split()[0])+float(g[i].split()[1]))/2)
      errtime.append((float(g[i].split()[1])-float(g[i].split()[0]))/2)
    elif t_measure == 'MJD':
      tavg.append((float(g[i].split()[2])+float(g[i].split()[3]))/2)
      errtime.append((float(g[i].split()[3])-float(g[i].split()[2]))/2)
    else:
      print('Not a valid choice, MET or MJD.')
      sys.exit()
    flux.append(float(g[i].split()[10]))
    errflux.append(float(g[i].split()[11]))
    conv.append(float(g[i].split()[13]))
    if conv[i] != 0:
      pl1flux.append(float(flux[i]))
      pl1time.append(float(tavg[i]))
    else:
      pl3flux.append(float(flux[i]))
      pl3fluxerr.append(float(errflux[i]))
      pl3time.append(float(tavg[i]))
      pl3terr.append(float(errtime[i]))

  try:
      plt.plot(pl1time, pl1flux, marker='x', color='r', ls='none')
  except:
      print 'All points succesfully converged!'
  plt.errorbar(pl3time, pl3flux, xerr=pl3terr,yerr=pl3fluxerr, marker='o', color='g', ls='none')
  plt.xlabel("Time in "+t_measure)
  plt.ylabel("Spectral Index")
  plt.title(file_title)
  plt.axis
  plt.show()
elif choice == 3:
  file_name = raw_input('Please enter lightcurve.txt file directory: ')
  file_title = raw_input('Enter title:')
  t_measure = raw_input('MET or MJD:')

  f = open(file_name,'r')    
  g = f.readlines()

  for i in range(0, len(g)):
    if t_measure == 'MET':
      tavg.append((float(g[i].split()[0])+float(g[i].split()[1]))/2)
      errtime.append((float(g[i].split()[1])-float(g[i].split()[0]))/2)
    elif t_measure == 'MJD':
      tavg.append((float(g[i].split()[2])+float(g[i].split()[3]))/2)
      errtime.append((float(g[i].split()[3])-float(g[i].split()[2]))/2)
    else:
      print('Not a valid choice, MET or MJD.')
      sys.exit()
    ts.append(float(g[i].split()[12]))
    conv.append(float(g[i].split()[13]))
    if conv[i] != 0:
      pl1flux.append(float(ts[i]))
      pl1time.append(float(tavg[i]))
    else:
      pl3flux.append(float(ts[i]))
      pl3time.append(float(tavg[i]))
      pl3terr.append(float(errtime[i]))

  try:
      plt.plot(pl1time, pl1flux, marker='x', color='r', ls='none')
  except:
      print 'All points succesfully converged!'
  plt.errorbar(pl3time, pl3flux, xerr=pl3terr, marker='o', color='g', ls='none')
  plt.xlabel("Time in "+t_measure)
  plt.ylabel("Test Statistic")
  plt.title(file_title)
  plt.axis
  plt.show()
else:
  print 'Not a valid choice!'
