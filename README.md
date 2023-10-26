### Source codes for paper:

# The practice of detecting potential space particles using CMOS cameras: hardware and algorithms

By Tomasz Hachaj, Marcin Piekarczyk

Source codes author: [Tomasz Hachaj](https://home.agh.edu.pl/~thachaj/)

Abstract: 


In this paper, we discuss a practice of potential cosmic ray detection using off-the-shelves CMOS cameras. We discuss and presents the limitations of up-to-date hardware and software approaches to this task. We also present a hardware solution that we made for long-term testing of algorithms for potential cosmic ray detection. We have also proposed, implemented and tested a novel algorithm that enables real-time processing of image frames acquired by CMOS cameras in order to detect tracks of potential particles. We have compared our results with already published results and obtained acceptable results overcoming some limitation of already existing algorithms. Both source codes and data are available to download.


Keywords: Cosmic rays detection, CMOS sensors, low-power devices, image processing

## Requirements

Hardware Raspberry PI >=3, Raspberry PI Camera (tested on 1.3 and 2.0)

OpenCV

## How to run

- Connect the camera to hardware (we used Raspberry PI 3.0 and Raspberry PI cameras 1.3 and 2.0)
- Compile C++ code [image_capture.cpp](raspberry_pi_code/image_capture.cpp)
- Run bash script [restart.sh](raspberry_pi_code/restart.sh)
- After capturing enough data run analysis found in folder [data_analysis](data_analysis/)

### Example potential particles detected by software

Raspberry PI camera 1.3

![alt text](<data_analysis/data/cropped/rp13/1 294 146.799316.png>) 
![alt text](<data_analysis/data/cropped/rp13/102 360 256.956268.png>)
![alt text](<data_analysis/data/cropped/rp13/1033 404 184.884628.png>) 
![alt text](<data_analysis/data/cropped/rp13/105 577 389.216522.png>)
![alt text](<data_analysis/data/cropped/rp13/73 467 351.805939.png>) 
![alt text](<data_analysis/data/cropped/rp13/743 419 226.178711.png>)

Raspberry PI camera 2.0

![alt text](<data_analysis/data/cropped/rp20/992 464 162.237442.png>) 
![alt text](<data_analysis/data/cropped/rp20/99 338 141.950699.png>)
![alt text](<data_analysis/data/cropped/rp20/9650 578 163.062180.png>) 
![alt text](<data_analysis/data/cropped/rp20/9612 332 120.886620.png>)
![alt text](<data_analysis/data/cropped/rp20/9550 289 93.348083.png>) 
![alt text](<data_analysis/data/cropped/rp20/9462 513 186.837463.png>)

## Cite as

Hachaj, Tomasz, and Marcin Piekarczyk. 2023. "The Practice of Detecting Potential Cosmic Rays Using CMOS Cameras: Hardware and Algorithms" Sensors 23, no. 10: 4858. https://doi.org/10.3390/s23104858 


@Article{s23104858,\
AUTHOR = {Hachaj, Tomasz and Piekarczyk, Marcin},\
TITLE = {The Practice of Detecting Potential Cosmic Rays Using CMOS Cameras: Hardware and Algorithms},\
JOURNAL = {Sensors},\
VOLUME = {23},\
YEAR = {2023},\
NUMBER = {10},\
ARTICLE-NUMBER = {4858},\
URL = {https://www.mdpi.com/1424-8220/23/10/4858}, \
PubMedID = {37430771},\
ISSN = {1424-8220},\
DOI = {10.3390/s23104858}\
}




