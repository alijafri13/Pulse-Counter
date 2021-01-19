# Pulse-Counting and behavioral tracking: Cassiopea Jellyfish

## Overview
The pulse-counter program is a frame by frame based analysis program that recognizes pulses for a jellyfish over a course of time. As Cassiopea pulse,the relaxation and 
contraction of the bell results in a change in average pixel intensity. The jellyfish are dark against a white background. 

## Installation
For easiest use, clone the repository and open program files on an IDE (pycharm, etc.). An additional shell file has been added for Linux and macOS users to run 
without and IDE. 

 ##### **IDE setup**
 For those using an IDE, python3 must be configured as your interpreter and additional packages must be installed inlcuding but not limited to matplotlib, scipy,
 sci-kit image, opencv-python among others. Import these packages from your interpreter settings. 
 
 ##### **Terminal setup**
 For package installation locally you can type the command `pip install <package name>`. In the directory where the shell file is located, you may run the 
 shell script with the command `$ bash execute.sh`
 
 ## Directory Organization
 For proper execution of code, directory setup is crucial. In a home directory, two folders must be present: one folder containing your frames and another folder 
 containing your ouputs. The video folder may contain folders of frames within them. Output folders must have two folders present: Analyzed and TXT.
 
 ## Execution
 #### Inputs to change in Intensity_Extractor
 - ftype
 - directory (this is the directory where videos are)
 - path2 (this path leads to your text file)
#### Inputs to change in Peak_Finder 
- path (this is the path to the output directory)
-path_for_length (path to videos)

* Note for IDE users: run JF_Instensity_Extractor first followed by JF_Peak_Finder *

While executing, program will prompt to select how many jellyfish to analyze. The inputted number should be the number of desired jellyfish to count plus 1 
that accounts for background subtraction. After appropriate number selection proceed to make selections always selecting from top left to bottom right. After 
selection, output TXT files will be generated. Execute JF_Peak_Finder which will prompt you to input which number jellyfish is desired to analyze. All files 
in the TXT file will be looped through and CSV's will be correspondingly generated. Printed statements indicate how many pulses the selected jellyfish made. 

