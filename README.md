Curve Fitting Assignment

Problem Statement
Given a dataset of points (x, y) that lie on a parametric curve:

x = t*cos(θ) - e^(M|t|)*sin(0.3t)sin(θ) + X
y = 42 + tsin(θ) + e^(M|t|)*sin(0.3t)*cos(θ)

Find the values of unknown parameters θ, M, and X that best fit the data in xy_data.csv.

Parameter Ranges

0° < θ < 50°
-0.05 < M < 0.05
0 < X < 100
6 < t < 60

Approach

The parameters were estimated using Python and SciPy’s minimize function to minimize the L1 distance between predicted and actual (x, y) data.
Steps:

Loaded the dataset using Pandas

Defined the parametric equations

Used the L-BFGS-B optimization algorithm

Found θ, M, and X minimizing L1 error

Plotted the fitted curve using Matplotlib

Final Fitted Parameters
| Parameter | Symbol | Value               |
| --------- | ------ | ------------------- |
| Theta     | θ      | 0.4908 rad = 28.13° |
| M         | M      | 0.02138             |
| X         | X      | 54.90               |

Final Equation
x = t*cos(0.4908) - e^(0.02138|t|)*sin(0.3t)sin(0.4908) + 54.90
y = 42 + tsin(0.4908) + e^(0.02138|t|)*sin(0.3t)*cos(0.4908)

Valid for 6 ≤ t ≤ 60

Desmos Equation
(tcos(0.4908) - e^(0.02138abs(t))sin(0.3t)sin(0.4908) + 54.90,
42 + tsin(0.4908) + e^(0.02138abs(t))*sin(0.3t)*cos(0.4908))

Desmos Link
Desmos Graph:https://www.desmos.com/calculator/dgloxvejb3

Tools Used

Python

NumPy

Pandas

SciPy

Matplotlib
