#This is a tool to plot files directly from a light curve file (binned or unbinned)
#Edited by: Eddie Solares
#Version 1.5

import numpy as np
import matplotlib.pyplot as plt
import sys

print("Welcome to the plot generator 1.5.")
print("""
      1 - Flux vs Time (PL2 method)
      2 - Flux vs Time (flux method)
      3 - EFlux vs Time
      4 - Index vs Time
      5 - TS vs Time
      """)
choice = input("Please choose one of the five: ")
file_name = raw_input('\nEnter the lightcurve text file directory: ')
file_title = raw_input('Enter the desired title: ')

for i in range(0, len(g)):
    time = ((float(g[i].split()[0])+float(g[i].split()[1]))/2)
    terr = ((float(g[i].split()[1])-float(g[i].split()[0]))/2)

if choice == 1:
  f = open(file_name,'r')    
  g = f.readlines()
  tavg  = list()
  flux    = list()      
  errflux = list()
  errtime = list()
  
  for i in range(0, len(g)):
    tavg.append(time)
    flux.append(float(g[i].split()[4]))
    errflux.append(float(g[i].split()[5]))
    errtime.append(terr)

  plt.errorbar(tavg, flux, xerr=errtime, yerr=errflux, fmt='s')
  plt.xlabel("Time in "+t_param)
  plt.ylabel("Flux >0.1 GeV (ph cm^-2 s^-1)")
  plt.title(file_title)
  plt.axis
  plt.show()
elif choice == 2: 
  f = open(file_name,'r')    
  g = f.readlines()
  tavg  = list()
  flux    = list()      
  errflux = list()
  errtime = list()
  
  for i in range(0, len(g)):          
      tavg.append(time)
      flux.append(float(g[i].split()[6]))
      errflux.append(float(g[i].split()[7]))
      errtime.append(terr)
	  
  plt.errorbar(tavg, flux, xerr=errtime, yerr=errflux, fmt='s')
  plt.xlabel("Time in "+t_param)
  plt.ylabel("Flux >0.1 GeV (ph cm^-2 s^-1)")
  plt.title(file_title)
  plt.axis
  plt.show()
elif choice == 3:
  f = open(file_name,'r')    
  g = f.readlines()
  tavg  = list()
  eflux    = list()      
  eerrflux = list()
  errtime = list()
  
  for i in range(0, len(g)):          
      tavg.append(time)
      eflux.append(float(g[i].split()[8]))
      eerrflux.append(float(g[i].split()[9]))
      errtime.append(terr)
	  
  plt.errorbar(tavg, eflux, xerr=errtime, yerr=eerrflux, fmt='s')
  plt.xlabel("Time in "+t_param)
  plt.ylabel("Energy Flux >0.1 GeV (MeV cm^-2 s^-1)")
  plt.title(file_title)
  plt.axis
  plt.show()
elif choice == 4:
  f = open(file_name,'r')    
  g = f.readlines()
  tavg  = list()
  index    = list()      
  errindex = list()
  errtime = list()
  
  for i in range(0, len(g)):          
      tavg.append(time)
      index.append(float(g[i].split()[10]))
      errindex.append(float(g[i].split()[11]))
      errtime.append(terr)
	  
  plt.errorbar(tavg, energy, xerr=errtime, yerr=errenergy, fmt='s')
  plt.xlabel("Time in "+t_param)
  plt.ylabel("Photon Index")
  plt.title(file_title)
  plt.axis
  plt.show()
elif choice == 5:
  f = open(file_name,'r')    
  g = f.readlines()
  tavg  = list()
  ts = list()
  errtime = list()
  
  for i in range(0, len(g)):          
      tavg.append(time)
      ts.append(float(g[i].split()[12]))
      errtime.append(terr)
	  
  plt.errorbar(tavg, ts, xerr=errtime, fmt='s')
  plt.xlabel("Time in "+t_param)
  plt.ylabel("Test Statistic")
  plt.title(file_title)
  plt.axis
  plt.show()
else:
  print("\nNot a valid plot choice, exiting now.")
