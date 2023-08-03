# Sunscreen-Project
A project in which sunscreen was tested to determine the effectiveness of active ingredients and compare it to commercial sunscreens.
## TheUVSensor.ino
Download Arduino.ide on https://www.arduino.cc/en/software. The recommended version for this code is 2.1.1. Open the file using Arduino.ide. Verify and upload the software onto your Arduino Uno. The sensor will then detect the current voltage generated by UVR and return the values.
## Procedure
In order to make the UV sensor, the Arduino Uno and the UV sensor had to be connected through a breadboard. This was done by: Connecting the Arduino Uno’s GND to the breadboard’s (-) Pin, the Arduino’s 3.3C to the (+) Pin next to the (-) Pin, and the Arduino’s A0 to the 58h pin on the breadboard. The UV sensor is then added by: Connecting the UV sensor’s Out Pin to the 58j pin on the breadboard, the UV sensor’s (-) Pin to a (-) Pin on the breadboard, and the UV sensor’s (+) Pin to the breadboard’s (+) Pin next to the previous (-) Pin. In total, this uses 6 wires. The code is then uploaded onto the sensor.

First, the varying concentrations of the homemade ZO sunscreen must be formulated. This is done by adding the required amount of ZO to a plastic bowl, then adding the required amount of lotion and mixing thoroughly. Set aside and repeat for the next concentration. To view the table of amounts used in our experiment, please view Paper.tex.

We then cut out 11 plastic squares, drew 2in by 2 in squares on them using a black sharpie and labeled each one: Plastic, 0% ZO, 5% ZO, 10% ZO, 12% ZO, 15% ZO, 20% ZO, 25% ZO, 50% ZO, Banana Boat (Organic), and Cetaphil (Inorganic). 50mg of each sunscreen was weighed out and added to its respective square (keeping inside the black lines), with “Plastic” being left empty. 

To conduct the experiment, all equipment was taken outside. A base reading was recorded before testing the “Plastic” square. 4 readings were then taken under the “Plastic” square, with each reading being taken at a different spot on the square. This procedure was then done with each sunscreen, from base reading to 4 readings. 

## To Plot
The 4 python files each with SunscreenDataPlot in the title plot different values. Those that are current in the file are those that were aquired in our experiment. In order to run the files use:
python3 filename
in the terminal. For example, to run and save 25ZOvsCommercialPlot.py as a png, enter

cd SunscreenProject

cd Plots

git pull

cd

python3 25ZOvsCommercialPlot.py

This will save the corresponding plot to your computer: 25ZOvsCommercialPlot.png

## The Presentations and Paper
Both the presentations and paper are .tex files, they all require images in the Images directory:
cd SunscreenProject
cd Images
git pull
cd
The above commands should provide these files for you. Make sure they are in the same location as the .tex files and also where the files can be seen by your favorite code editor. 3 style files are needed for the side presentation: beamercolorthemeshark.sty, beamerinnerthemechamgered.sty, and beamerouterthemewuerzburg.sty. These 3 style files and side presentation are in the directory. In order to access and run the side project presentation type these 5 commands into the terminal:

cd SunscreenProject

cd SidePresentation

git pull

cd

pdflatex SideProjectCPresentation
To run the paper, type these commands into the terminal:

cd SunscreenProject

cd Paper

git pull

cd

pdflatex Paper
