#This is a python script for creating lightcurve text files for a unbinned likelihood analysis.
#If running on a command prompt window please create fermi directory prior to running this program.
#Edited by: Eddie E. Solares
#Version 4.2
#Now Updated for Pass 7


#Import all of the needed modules
import numpy
import pyLikelihood
import math
import pyfits
import sys
import os
from UpperLimits import UpperLimits
from gt_apps import *
from UnbinnedAnalysis import *
from make2FGLxml import *


#Beginning Messages
print('\nWelcome to the unbinned likelihood analysis.')
print('It is suggested that you combine event files before you start.')
option = raw_input('To quit the program type q and press enter, to continue press enter: ')
if option == 'q':
  sys.exit()
else:
  print('\n***Welcome to the unbinned light curve generator version 4.2!***')
  print("""\n
                                 __           ___                     
                  ___          /  /\         /__/\          ___       
                 /  /\        /  /:/_        \  \:\        /  /\      
  ___     ___   /  /:/       /  /:/ /\        \__\:\      /  /:/      
 /__/\   /  /\ /__/::\      /  /:/_/::\   ___ /  /::\    /  /:/       
 \  \:\ /  /:/ \__\/\:\__  /__/:/__\/\:\ /__/\  /:/\:\  /  /::\       
  \  \:\  /:/     \  \:\/\ \  \:\ /~~/:/ \  \:\/:/__\/ /__/:/\:\      
   \  \:\/:/       \__\::/  \  \:\  /:/   \  \::/      \__\/  \:\     
    \  \::/        /__/:/    \  \:\/:/     \  \:\           \  \:\    
     \__\/         \__\/      \  \::/       \  \:\           \__\/    
                               \__\/         \__\/                    
      ___           ___           ___                        ___      
     /  /\         /__/\         /  /\          ___         /  /\     
    /  /:/         \  \:\       /  /::\        /__/\       /  /:/_    
   /  /:/           \  \:\     /  /:/\:\       \  \:\     /  /:/ /\   
  /  /:/  ___   ___  \  \:\   /  /:/~/:/        \  \:\   /  /:/ /:/_  
 /__/:/  /  /\ /__/\  \__\:\ /__/:/ /:/___  ___  \__\:\ /__/:/ /:/ /\ 
 \  \:\ /  /:/ \  \:\ /  /:/ \  \:\/:::::/ /__/\ |  |:| \  \:\/:/ /:/ 
  \  \:\  /:/   \  \:\  /:/   \  \::/~~~~  \  \:\|  |:|  \  \::/ /:/  
   \  \:\/:/     \  \:\/:/     \  \:\       \  \:\__|:|   \  \:\/:/   
    \  \::/       \  \::/       \  \:\       \__\::::/     \  \::/    
     \__\/         \__\/         \__\/           ~~~~       \__\/     


  """)

#Change the directory of where all your files will be saved
print('\nPlease type the directory where your event and spacecraft files are located.')
script = raw_input('This will be the directory where all the files created will be stored: \n')
os.chdir(script)

#Recover from a previous crashed session
recover = raw_input("\nIf you want to recover type r, else press enter: ")
if recover == "r":
  #Input all the variables you need to run analysis
  name = raw_input('\nEnter name of object with no spaces: ')
  cat_name = raw_input('Enter name of catalog: 2FGLJ')
  event_file = raw_input('Enter the event file name: ')
  sc_file = raw_input('Enter the spacecraft file name: ')
  xml_file = raw_input('Enter xml_file name: ')

  try:
    t_start = input("Select the time where you would like to restart: ")
    bin_num = input("What bin is this?: ")
    radius = input('Enter ROI: ')
    energy_min = input('Enter minimum energy: ')
    energy_max = input('Enter max energy: ')
    binning = input('Enter bin parameter in seconds: ')
  except:
    print("You didn't enter a correct value, exiting now.")
    sys.exit()
   
  #Second stage of input
  try:
    sc = pyfits.open(sc_file)
  except:
    print("The directory for the spacecraft file is incorrect, exiting now.")
    sys.exit()
  
  #Third stage of input
  start = t_start
  end = sc[0].header['TSTOP']
  
  #Set the start time of the first bin to the MET tstart value
  bin_start = start
  bin_stop = start + binning
  this_bin = bin_num
  
#Normal mode if no restore option  
else:
  #Input all the variables you need to run analysis
  name = raw_input('\nEnter name of object with no spaces: ')
  cat_name = raw_input('Enter name of catalog: 2FGLJ')
  event_file = raw_input('Enter the event file name: ')
  sc_file = raw_input('Enter the spacecraft file name: ')
  xml_file = raw_input('Enter xml_file name: ')
  
  try:
    radius = input('Enter ROI: ')
    energy_min = input('Enter minimum energy: ')
    energy_max = input('Enter max energy: ')
    binning = input('Enter bin parameter in seconds: ')
  except:
    print("You didn't enter a correct value, exiting now.")
    sys.exit()
  
  #Second stage of input
  try:
    sc = pyfits.open(sc_file)
  except:
    print("The directory for the spacecraft file is incorrect, exiting now.")
    sys.exit()
  
  #Third stage of input
  start = sc[0].header['TSTART']
  end = sc[0].header['TSTOP']  

  #Set the start time of the first bin to the MET tstart value
  bin_start = start
  bin_stop = start + binning
  this_bin = 0

#Main Loop
while (bin_stop < end ):
    folder = []
    folder.append(str(bin_start))											#Start time in MET
    folder.append(" ")
    folder.append(str(bin_stop))											#Stop time in MET
    folder.append(" ")
    folder.append(str(51910+(bin_start/86400)))										#Start time in MJD
    folder.append(" ")
    folder.append(str(51910+(bin_stop/86400)))										#Stop time in MJD
    folder.append(" ")
    
    print '\n***Working on range ('+str(bin_start)+','+str(bin_stop)+')***'
    
    print '\n***Running gtselect***'
    filter['evclsmin'] = 2
    filter['evclsmax'] = 2
    filter['ra'] = "INDEF"
    filter['dec'] = "INDEF"
    filter['rad'] = radius
    filter['emin'] = energy_min
    filter['emax'] = energy_max
    filter['zmax'] = 100
    filter['tmin'] = bin_start
    filter['tmax'] = bin_stop
    filter['infile'] = str(event_file)
    filter['outfile'] = str(name)+'select'+str(this_bin)+'.fits'
    filter.run()

    print '\n***Running gtmktime***'
    maketime['scfile'] = sc_file
    maketime['filter'] = '(DATA_QUAL==1)&&(LAT_CONFIG==1)&&ABS(ROCK_ANGLE)<52'
    maketime['roicut'] = 'yes'
    maketime['evfile'] = str(name)+'select'+str(this_bin)+'.fits'
    maketime['outfile'] = str(name)+'mktime'+str(this_bin)+'.fits'
    maketime.run()

    print '\n***Running gtltcube***'
    expCube['evfile'] = str(name)+'mktime'+str(this_bin)+'.fits'
    expCube['scfile'] = str(sc_file)
    expCube['outfile'] = str(name)+'ltcube'+str(this_bin)+'.fits'
    expCube['dcostheta'] = 0.025                                                 
    expCube['binsz'] = 1                                          
    expCube.run()

    print '\n***Running gtexpmap***'
    expMap['evfile'] =  str(name)+'mktime'+str(this_bin)+'.fits'
    expMap['scfile'] = str(sc_file)
    expMap['expcube'] = str(name)+'ltcube'+str(this_bin)+'.fits'
    expMap['outfile'] = str(name)+'expmap'+str(this_bin)+'.fits'
    expMap['irfs'] ='P7SOURCE_V6'
    expMap['srcrad'] = radius + 10
    expMap['nlong'] =120
    expMap['nlat'] =120
    expMap['nenergies'] = 20
    expMap['debug'] = 'yes'
    expMap.run()
    
    
    print '\n***Running likelihood analysis***'
    try:
    	obs = UnbinnedObs(str(name)+'mktime'+str(this_bin)+'.fits',str(sc_file),expMap=str(name)+'expmap'+str(this_bin)+'.fits',expCube=str(name)+'ltcube'+str(this_bin)+'.fits',irfs='P7SOURCE_V6')
    	like1 = UnbinnedAnalysis(obs,str(xml_file),optimizer='DRMNFB')							
    	like1.fit(verbosity=0)
    	like1.logLike.writeXml(str(name)+'fit'+str(this_bin)+'.xml')
    	like2 = UnbinnedAnalysis(obs,srcModel=str(name)+'fit'+str(this_bin)+'.xml',optimizer='NewMinuit')
    	obj = pyLike.Minuit(like2.logLike)
    	like2.fit(verbosity=0, covar=True, optObject=obj)
    	like2.plot()
    
    	try:														
      		flux = like2.model['_2FGLJ'+str(cat_name)].funcs['Spectrum'].getParam('Integral').value()
      		errFlux = like2.model['_2FGLJ'+str(cat_name)].funcs['Spectrum'].getParam('Integral').error()
      		scale = like2.model['_2FGLJ'+str(cat_name)].funcs['Spectrum'].getParam('Integral').getScale()
    	except:
      		flux = 0
      		errFlux = 0
      		scale = 0
    	ratio1 = like2.fluxError('_2FGLJ'+str(cat_name),emin=energy_min, emax=energy_max)
    	ratio2 = like2.flux('_2FGLJ'+str(cat_name),emin=energy_min, emax=energy_max)
    	ults = like2.Ts('_2FGLJ'+str(cat_name))
    	scaled_flux = flux*scale
    	scaled_errFlux = errFlux*scale
    	ulfr = ratio1/ratio2
    
    
    	folder.append(str(scaled_flux))												#Flux xml
    	folder.append(" ")
    	folder.append(str(scaled_errFlux))											#Flux xml Error
    	folder.append(" ")
    	folder.append(str(like2.flux('_2FGLJ'+str(cat_name),emin=energy_min, emax=energy_max)))					#Flux method
    	folder.append(" ")
    	folder.append(str(like2.fluxError('_2FGLJ'+str(cat_name),emin=energy_min, emax=energy_max)))				#Flux method error
    	folder.append(" ")
    	folder.append(str(like2.energyFlux('_2FGLJ'+str(cat_name),emin=energy_min, emax=energy_max)))				#Energy Flux method
    	folder.append(" ")
    	folder.append(str(like2.energyFluxError('_2FGLJ'+str(cat_name),emin=energy_min, emax=energy_max)))			#Energy Flux method error
    	folder.append(" ")
    	folder.append(str(like2.model['_2FGLJ'+str(cat_name)].funcs['Spectrum'].getParam('Index').value()))			#Index
    	folder.append(" ")
    	folder.append(str(like2.model['_2FGLJ'+str(cat_name)].funcs['Spectrum'].getParam('Index').error()))			#Index Error
    	folder.append(" ")
    	folder.append(str(like2.Ts('_2FGLJ'+str(cat_name))))									#Test Statistic
    	folder.append(" ")
    	folder.append(str(obj.getRetCode()))											#Convergence Test
    	folder.append(" ")
    	folder.append(str(obj.getQuality()))											#Fit Quality
    	folder.append(" ")
    
    	if ults < 10 or ulfr > 0.5:												#Upper Limits
      		ul = UpperLimits(like2)
      		ul['_2FGLJ'+str(cat_name)].compute(emin=energy_min,emax=energy_max)
      		folder.append(str(ul['_2FGLJ'+str(cat_name)].results[0]))
    	else:															#Upper Limits Alternative
      		folder.append(str(0))
      
    	folder.append("\n")													#New line for new loop
    
    	txt = open(str(name)+"light_curve.txt","a")
    	txt.writelines(folder)
    	txt.close()

    	#Deletes Unecessary files that take up disk space
    	del like1
    	del like2
    	del flux
    	del errFlux
    	del scale
    	del scaled_flux
    	del scaled_errFlux
    	del obs
   	del folder
    	os.remove(str(name)+'select'+str(this_bin)+'.fits')
    	os.remove(str(name)+'mktime'+str(this_bin)+'.fits')
    	os.remove(str(name)+'ltcube'+str(this_bin)+'.fits')
    	os.remove(str(name)+'expmap'+str(this_bin)+'.fits')
    	os.remove(str(name)+'fit'+str(this_bin)+'.xml')

    except:
    	print 'WARNING: Likelihood Analysis Failed - now switching to next bin...'

    bin_start = bin_stop
    bin_stop += binning
    this_bin += 1

