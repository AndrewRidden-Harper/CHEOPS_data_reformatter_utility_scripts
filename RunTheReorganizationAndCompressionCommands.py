#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 12:58:38 2022

@author: Andrew Ridden-Harper

This script is the second of 2 for converting CHEOPS data downloaded from the 
CHEOPS archive into a format that can be read by the PyCHEOPS example notebook.

The first script is RenameDownloadedZipFiles.py

This script:
    
    1: Unzips the file 
    2: creates a directory with the same name minus the leading ("CH_")
    3: Compresses the newly created directory into a .tgz (tar.gzip) file 
       with name including the leading "CH_"
    4: Deletes the temporary files 
"""

import os 

ZipLoadDir = 'AndrewInitialZipFiles'



ListOfFilesToDo = os.listdir(ZipLoadDir)
ListOfFilesToDo.sort()


for i in range(len(ListOfFilesToDo)):
#for i in [0,1]:
    
    if i > 0:
        os.chdir('../') ### Go back out of the UncompressedZipFiles directory for the next iteration of this loop

    
    FileNameZip = ListOfFilesToDo[i]
    
    FileNameNoExt = FileNameZip[0:-4]
    
    FileNameNoCH = FileNameNoExt[3:]
    
    UncompressedZipOutputDirectory = 'UncompressedZipFiles/%s'%(FileNameNoExt)
    ZipToUncompress = '%s/%s'%(ZipLoadDir,FileNameZip)
    
    
    ## unzip file.zip -d destination_folder    
    UnzipCommand = 'unzip %s -d %s'%(ZipToUncompress,UncompressedZipOutputDirectory)
    
    CommandToMoveForRename = 'mv UncompressedZipFiles/%s UncompressedZipFiles/%s  '%(FileNameNoExt,FileNameNoCH)

    
    os.system(UnzipCommand)
    os.system(CommandToMoveForRename)
    
    ### tgz compression needs to be done in its directory   
    os.chdir('UncompressedZipFiles') ### Change the working directory into UncompressedZipFiles
    CommandToDoTgzCompression = 'tar -czvf %s.tgz %s'%(FileNameNoExt,FileNameNoCH)      
    os.system(CommandToDoTgzCompression)
    
    ### Needed for Jake's file names without the leading 0
    #NameWithLeadingVersionZero = FileNameNoExt[0:22] + '0' + FileNameNoExt[22:] + '.tgz'  
    
    ### For my file names with the leading zero
    NameWithLeadingVersionZero = FileNameNoExt + '.tgz'
    
    CommandToMoveAndRenameTgzFile = 'mv %s.tgz ../TgzFiles/%s'%(FileNameNoExt,NameWithLeadingVersionZero)
    os.system(CommandToMoveAndRenameTgzFile)
    
    CommandToDeleteUncompressedZipFiles = 'rm -r %s'%(FileNameNoCH)
    os.system(CommandToDeleteUncompressedZipFiles)

    



    
