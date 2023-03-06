### Source codes for paper:

# The practice of detecting potential space particles using CMOS cameras: hardware and algorithms

Author: [Tomasz Hachaj](https://home.agh.edu.pl/~thachaj/)

Abstract: TO BE ADDED

Keywords: Cosmic rays detection, CMOS sensors, low-power devices, image processing

## Requirements

Hardware Raspberry PI >=3, Raspberry PI Camera (tested on 1.3 and 2.0)

OpenCV

## How to run

- Connect the camera to hardware (we used Raspberry PI 3.0 and Raspberry PI cameras 1.3 and 2.0)
- Compile C++ code [image_capture.cpp](raspberry_pi_code/image_capture.cpp)
- Run bash script [restart.sh](raspberry_pi_code/restart.sh)
- After capturing enough data run analysis found in folder [data_analysis](data_analysis/)

### Example particles detected by software

Raspberry PI camera 1.3

![alt text](<data_analysis/data/cropped/rp13/1 294 146.799316.png>) 
![alt text](<data_analysis/data/cropped/rp13/102 360 256.956268.png>)
![alt text](<data_analysis/data/cropped/rp13/1033 404 184.884628.png>) 
![alt text](<data_analysis/data/cropped/rp13/105 577 389.216522.png>)
![alt text](<data_analysis/data/cropped/rp13/107 273 102.238930.png>) 
![alt text](<data_analysis/data/cropped/rp13/1075 301 147.868256.png>)

Raspberry PI camera 2.0

## Cite as

TO BE ADDED