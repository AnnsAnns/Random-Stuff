#!python3
import os, sys
import time
from PIL import Image

print("Bootimage Converter for Hekate")
print("------------------------------")
print("By @_tomGER / tumGER on Github")
print("\nI hope that you actually dragged a file onto this!")
time.sleep(5)
print("\nAnyways - File will probably be processed now")
time.sleep(1)

for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = "bootlogo.bmp"
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print("Cannot convert", infile)
# You're asking yourself why I'm saving the file 2 times?
# Because I can :P
    src_im = Image.open(outfile)
    size = 720, 1280
    rot = src_im.rotate(90, expand=1).resize(size)
    rot.save(outfile)