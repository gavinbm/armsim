# armsim
My attempt at making an ARMv8 simulator like the one found here https://github.com/d-gaston/armv8-examples

Most Recent Updates
===============================================
  Branches have been implemented via a dictionary
  that pairs labels (keys) to line numbers in input.txt (values)
  Not very memory efficient since it uses a dictionary

  Going to work on a stack implementation for ldr and str instructions

Long term plan is to put this on a website where users can input ARMv8 code and see what happens to the stack and registers to help them learn how ARM asm works.
