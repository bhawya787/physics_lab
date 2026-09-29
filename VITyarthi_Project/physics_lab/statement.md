# Problem Statement

## Problem statement
Students in school and first year college labs keep repeating the same physics formulas by hand. It takes time, small mistakes creep in, and it is hard to check an answer quickly while doing an experiment write up. There is a need for a small tool that does these calculations correctly and lets the student focus on understanding the physics.

## Scope of the project
The project is a command line Python program that covers five standard physics experiments:

1. Projectile motion
2. Simple pendulum
3. Radioactive decay
4. Series LCR circuit
5. Image formation by a concave lens

The program only does calculations from the values the user types in. It does not read data from sensors, does not draw graphs and does not have a GUI. Standard textbook formulas are used, with g fixed at 9.8 m/s^2 and ideal conditions (no air resistance, small swing angle for the pendulum, thin lens).

## Target users
- School students (class 11 and 12) doing physics practicals
- First year college students
- Teachers who want a quick way to check answers

## High level features
- Menu based program that runs fully in the terminal
- Five experiment modules, each with its own calculations
- Input checking, so wrong or silly values do not crash the program
- Every calculation is saved to a log file (lab_log.txt) with a timestamp
- Unit tests for every experiment and for the input checker
