# Lift Coursework
This project simulates a lift under three algorithms, a simple one (SCAN), an extension of SCAN with added functionality (LOOK), and a complex one (MYLIFT).
Each algorithm simulates addressing requests made on a variable number of floors and how the lift acting under the contraints of the algorithm will address
such requests. Some constraints include:
- The capacity of the lift
- The direction the lift is travelling

## Features
1. The SCAN algorithm simply travels up and down, picking and dropping off people when it can
2. The LOOK algorithm acts the same, except with the added functionality of being able to look ahead on it's current trajectory to see if there are any more
requests that need to be served or whether it can change direction early
3. The MYLIFT algorithm surpassed both, being completed differently designed from the ground up to search for the most 'valuable' floor it could go to,
then to go, taking into account capacity, distance and requests.
All algorithms use data structures to cohesively sort data, such as stacks, queues and priority queues, so that the lift may move more efficiently.

## Expected Input and Output
The template input files can be seen in input1.txt, input2.txt and input3.txt, following the same structure, with variable floors and requests.
These input files are then re-structured to be more accessible for the algorithms in Main.py, then implemented in the algorithms which return time_intervels tracking
the efficiency of the algorithm to Main.py.
This output data is then used in plotting_graphs.py to visually show the differences in the approaches.

### Implementation
To run the project, use either the input files or import your own in txt format following the template of the input files. Change the file being used in the function fileread() in main to change what input it takes, and change what algorithm you would like to use in the main() function in main.py. The output data will then be appended to data.txt which can then be used in plotting graphs to visualise the data.

### Authors
Zachary Fenton
Sebastian Leach
Steffan Griffiths

This Coursework is licensed under APACHE 2.0


