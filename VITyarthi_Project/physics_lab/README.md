# Physics Experiment Calculator

## Overview
A simple command line program in Python that does the calculations for five common physics experiments. You pick an experiment from a menu, type in the values, and the program prints the results. It works only with the Python standard library, so there is nothing extra to install.

## Features
- Projectile motion: velocity in x direction, initial velocity in y direction, time of flight, maximum height, range
- Simple pendulum: time period and frequency
- Radioactive decay: decay constant, mean life (tau), amount remaining and amount decayed
- Series LCR circuit: reactances, impedance, current, phase angle, resonant frequency, quality factor
- Concave lens: image distance, magnification, image height and nature of the image
- Input checking for every value (text, zero, negative, nan and inf are all rejected)
- Every calculation is saved in `lab_log.txt`

## Technologies used
- Python 3.8 or newer
- Standard library only: `math`, `logging`, `unittest`
- Git and GitHub for version control

## Project structure
```
physics_lab/
    main.py
    helpers/
        inputs.py
        output.py
    experiments/
        projectile.py
        pendulum.py
        decay.py
        lcr.py
        lens.py
    tests/
        test_experiments.py
        test_inputs.py
    README.md
    statement.md
```

## How to install and run
1. Make sure Python 3.8 or newer is installed. Check with:
   ```
   python --version
   ```
   On some systems the command is `python3`.
2. Clone the repository and go inside the folder:
   ```
   git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
   cd YOUR-REPO-NAME
   ```
3. There are no packages to install and no configuration is needed.
4. Run the program:
   ```
   python main.py
   ```
5. Type a number from 1 to 6 to pick an experiment (6 exits), then type the values it asks for.

## Sample run
```
=== Physics Experiment Calculator ===

1. Projectile motion
2. Simple pendulum
3. Radioactive decay
4. LCR circuit
5. Concave lens image
6. Exit
pick an option: 1
Projectile Motion
initial speed in m/s: 25
launch angle in degrees (0 to 90): 45

--- Projectile Motion Results ---
Velocity in x direction                  17.6777 m/s
Initial velocity in y direction          17.6777 m/s
Time of flight                            3.6077 s
Maximum height                           15.9439 m
Horizontal range                         63.7755 m
```

## How to run the tests
From the main project folder run:
```
python -m unittest discover -s tests -v
```
All 20 tests should pass. If you are on Linux or Mac and `python` does not work, use `python3`.

## Log file
After each calculation a line is added to `lab_log.txt` in the folder you ran the program from. It is created automatically the first time you finish a calculation.

## Formulas used
- Projectile: vx = v cos(a), vy = v sin(a), T = 2 vy / g, H = vy^2 / 2g, R = vx T
- Pendulum: T = 2 pi sqrt(L / g)
- Decay: lambda = ln2 / half life, tau = 1 / lambda, N = N0 e^(-lambda t)
- LCR: XL = 2 pi f L, XC = 1 / (2 pi f C), Z = sqrt(R^2 + (XL - XC)^2), I = V / Z, tan(phi) = (XL - XC) / R, f0 = 1 / (2 pi sqrt(LC)), Q = (1/R) sqrt(L/C)
- Concave lens: 1/v - 1/u = 1/f with f and u negative, m = v / u
