 #!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script for extracting changes in pixel intensity of individual jellyfish
over time.

@author: Claire Bedbrook & Ravi Nath

"""
from __future__ import division, absolute_import, \
                                    print_function, unicode_literals
                                    
import os
import numpy as np
import scipy.signal
import matplotlib.pyplot as plt
from matplotlib import cm
import skimage.io
import jb_utils as jb
import cv2
from pathlib import Path
import pandas as pd

# A whole bunch of skimage stuff
#import skimage.feature
#import skimage.filters
#import skimage.filters.rank
#import skimage.io
#import skimage.morphology
#import skimage.restoration
#import skimage.segmentation

################################################################################
#### path contains raw images, intensity measurments are written to path2  #####
################################################################################
# Input DATE, DAY or NIGHT, CAMERA, and file type
# date = '20170621'
# time = 'day'
# camera = 'cam2'

# ftype = '.TIF'
ftype = '.jpg'
ROI = 'small'

#directory = '/Volumes/External/Research/Jellyfish/Pulse_Counter/Videos/'
directory =  'E:/Video_Archive/Chemical_Screens/Gaboxadol/20210224/Image_Stacks/20210224_605pm_baseline/'
all_videos = []
#for file in os.scandir(directory):
    #all_videos.append(file.path + '/')
#for i in all_videos[::2]:
    #print(type(i))
length = os.listdir(directory) # dir is your directory path
number_files =len(length)
print(number_files)
# path = '/Volumes/External/Jellyfish/Pulse_Counter_Videos/Example_TIF/'
path = directory

# path2 = '/Volumes/External/Jellyfish/Pulse_Counter_Videos/Output/TXT'
path2 = 'E:/Video_Archive/Chemical_Screens/Gaboxadol/20210224/Outputs/TXT/'



tail = os.path.basename(os.path.normpath(path))

# open(Path(path2 + tail + '.txt'))
#open(os.path.join(path2 + tail + '.txt'),'w')
#
################################################################################
########## Process 20 min of data for the first 20 min of each hour ############
################################################################################
# at 15 fps 18,000 frames represents ~20 min
sl = 20

## roughly 7:15 AM, Morning
jp1 = 1

# roughly 8:15 AM
jp2 = 54000

# roughly 9:15 AM, Mid day
jp3 = 108000

# roughly 10:15 AM
jp4 =  162000

# roughly 11:15 AM
jp5 =  216000

# roughly 12:15 PM
jp6 =  270000

# roughly 1:15 PM
jp7 =  324000

# roughly 2:15 PM
jp8 =  378000

# roughly 3:15 PM
jp9 =  432000

# roughly 4:15 PM
jp10 =  486000

# roughly 5:15 PM
jp11 =  540000

# roughly 6:15 PM
jp12 =  594000

jp13 = 648000

jp14 = 702000

jp15 = 756000

jp16 = 810000

jp17 = 864000

jp18 = 918000

jp19 = 972000

jp20 = 1026000

jp21 = 1080000

jp22 = 1134000

jp23 = 1188000

jp24 = 1242000

jp25 = 1296000

#### list of slices ############################################################
# slst = [[jp1, jp1 + sl], [jp2, jp2 + sl], [jp3, jp3 + sl], [jp4, jp4 + sl], \
#         [jp5, jp5 + sl], [jp6, jp6 + sl], [jp7, jp7 + sl], [jp8, jp8 + sl], \
#         [jp9, jp9 + sl], [jp10, jp10 + sl], [jp11, jp11 + sl], \
#         [jp12, jp12 + sl]]

slst = [[jp23, jp23+sl]]

#slst = [[54000,54000+18000]]

#### Jumping through slice list ################################################
mat = []
for t in range(len(slst)):
    ############################################################################
    ####### JFC: Jellyfish Condos: top right and bottom left coordinates #######
    ############################(x1, x2, y1, y2) ###############################
    ################# We will need to update this each time ####################
    ############################################################################
    plt.close('all')
    JFC = []
    # Normally 9 JFCs, 8 Condos & 1 Background
    #condos = int(input('How many condos to analyze for ' + tail + '?'))
    condos =3
    for each in range(condos):
        # first image
        img_1 = skimage.io.imread(path + '' + str(slst[t][0])  + ftype)
        # last image
        #img_2 = skimage.io.imread(path + '' + str(slst[t][1])  + ftype)
        skimage.io.imshow(img_1)
        #skimage.io.imshow(img_2)
        # plt.show()
        plt.draw()
        # maybe switch draw and show??
        """
        coordinates are not showing up as you make clicks
        """
        #### NOTE: timeout=0 prevents time out AND use delete/backspace to undo
        ####       a bad click!

        JFC.append((plt.ginput(2, timeout=0)))
        ### Use pic to iterate because there is no Frame_0

    plt.close('all')

    try:
        JFC = np.array(JFC)
        JFC = JFC.astype(int)
        for i in range(slst[t][0], slst[t][1]):
        # for i in range(1,10):
            data = cv2.imread(path + '' + str(i) + ftype)
    # This list will be filled with JFC mean pixel intensity measurments
            lst = []
            alst = []
    # Iterates through 12 (timepoints) JFC ROI
            for item in JFC:
                # items in printed JFC = [[(25.173578307674646, 113.33912000242725), (88.99688230863492, 155.50808871734745)], [(108.04331022291606, 131.6187152962505), (125.13665815194472, 148.71206322527917)]]
                imean = (np.mean(data[item[0][1]:item[1][1], item[0][0]:item[1][0]]))
                print(imean)
                # imean = imean * -1
                iarea = (item[1][0] - item[0][0]) * (item[1][1] - item[0][1])
                # all the means
                lst.append(imean)

                # all the areas
                alst.append(iarea)


            mat.append(lst + alst)
        print(mat)
            # print('pic:  ' + str(i))

    except:
        # print('pass')

        pass
    print('processed ' + tail)
    # print('loop: ' + str(t))

################################################################################
######## Writing our matrix of ROI measurments for all frames to a file ########
################################################################################
if __name__ == "__main__":
    # Will create 4 files, each file will have our 'jump' info
    count = 0
    for t in range(len(slst)):
        # Creating File
        #path2 = os.path.abspath(path2)
        w = open(os.path.join(path2 +
        #                       \
        # date + '_' + time  + '_' + camera + '_' +
                              tail+ "test" + '.txt'), 'w')
        # w.write(date + ' ' + time  + ' ' + camera)
        w.write('\n' + ROI + '\n')

        # Adding Jellyfish Columns
        for column in range(int(len(mat[0])/2)):
            w.write('J' + str(column) +'\t' )

        # Adding Area Columns
        for column in range(int(len(mat[0])/2)):
            w.write('J' + str(column) +'area' +'\t' )

        # Adding Values for Jellyfish
        for row in mat[count: count + sl]:
            w.write('\n')
            for num in row:
                w.write('%.1f\t' % num)


        count += sl

        w.close()