# face-recognition--girlscript-jaipur-project-
In this project , I have tried to code in python to  make computer recognise human faces.
Subparts Includes "IMAGE DETECTION", IMAGE TRACKING", "IMAGE RECOGNISING"  
LIBRARIES USED:
          numpy
          opencv 
          os
          haarcascade_frontalface_default.xml
          haarcascadeeye.xml
          
## ACKNOWLEDGEMENT 
haar cascade files which I have used, and will be using in other projects are uploaded.
face_detect         - This includes the code, that traces / identifies your face
eye_detect          - This includes the code, that traces / identifies your face and eyes
face_recog_dataset  - file that detects faces, and then clicks pictures, converts to grayscale, and saves it into datasets folder(create a                       folder name datasets, where you have saved all these files, or otherwise it will show error)
face_recog_train    - it trains model over images saved in folder datasets
face_recog_test     - testing for recognizing faces from the dataset
trainingdata.yml    - trained data is saved in this file
