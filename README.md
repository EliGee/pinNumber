# pinNumber
Python draft attempting to generate a 6-digit, easy-to-remember pin 

It's a six digit pin where every pair of digits is a fairly easy-to-remember number
     A:   one number ends in 0 (20, 30, 50, etc.)
     B:   one consists of two repeated digits (22, 33, 55, etc.)
     C:   one consistents of a pair of either even or odd numbers consecutive (24, 35, 57, etc.)

The function for generating Variable C is working fine.  I'm using the same function for generating A and B, with the idea to just alter to integer it starts on (either 10 or 11) but keep the code the same.

I'm using list(x, y, z) to generate a list of numbers counting by 10 through just under 100, either 10, 20, 30...90 or 11, 22, 33... 99 
    x is supposed to be the argument of the function, and y and z are always 100 and 10, respectively

BUT I GET THIS ERROR, AS IF BECAUSE I'M USING A FUNCTION THAT ONLY TAKES ONE ARGUMENT, I'M NOT ALLOWED TO USE LIST(X, Y, Z), BECAUSE IT TAKES 3 ARGUMENTS???!
Traceback (most recent call last):
  File "C:\\Users\\eilee\\OneDrive\\Documents\\My_code\\pinRandomizer.py", line 72, in <module>
    pinBitA = generateIncrements(10)
  File "C:\\Users\\eilee\\OneDrive\\Documents\\My_code\\pinRandomizer.py", line 34, in generateIncrements
    countList = list(start, 100, 10)
TypeError: list expected at most 1 argument, got 3"""

Please kill me. 
    -E
