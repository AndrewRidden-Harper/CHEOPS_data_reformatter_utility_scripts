#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 16:14:04 2022

@author: Andrew Ridden-Harper


This script is the first of 2 for converting CHEOPS data downloaded from the 
CHEOPS archive into a format that can be read by the PyCHEOPS example notebook.

This script:
    
    1: Unzips the .zip file
    2: Gets the required file name from the zip file contents
    3: Renames the .zip file
    4: Deletes the unzipped folder 
    
Next use:
    RunTheReorganizationAndCompressionCommands.py
    
"""


import os 

ZipLoadDir = 'DownloadedZipFiles'


ListOfFilesToDo = os.listdir(ZipLoadDir)
ListOfFilesToDo.sort()


for i in range(len(ListOfFilesToDo)):
#for i in [0]:    
    
    FileNameZip = ListOfFilesToDo[i]

    
    UncompressedZipOutputDirectory = 'ZipTempDir'
    
    if os.path.exists(UncompressedZipOutputDirectory):
        #os.rmdir(UncompressedZipOutputDirectory)
        os.system('rm -r %s'%(UncompressedZipOutputDirectory))
    
    ZipToUncompress = '%s/%s'%(ZipLoadDir,FileNameZip)
    
    DownloadedZipFileName = ListOfFilesToDo[i]
    
    UnzipCommand = 'unzip %s -d %s'%(ZipToUncompress,UncompressedZipOutputDirectory)
    
    os.system(UnzipCommand)
    
    TempUnzippedFiles = os.listdir(UncompressedZipOutputDirectory)
    TempUnzippedFiles.sort()
    
    NeededPartOfFileName = TempUnzippedFiles[0][0:20]
    
    NewFileName = '%s_V0200'%(NeededPartOfFileName)
    
    MoveCommand = 'cp %s/%s AndrewInitialZipFiles/%s.zip'%(ZipLoadDir,FileNameZip,NewFileName)
    
    os.system(MoveCommand)
    
    if os.path.exists(UncompressedZipOutputDirectory):
        #os.rmdir(UncompressedZipOutputDirectory)
        os.system('rm -r %s'%(UncompressedZipOutputDirectory))

    
    
