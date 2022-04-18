This Version comes with 4 modes which are selected using the runmode command. 

Generational mode: 
set runmode to 0 and you should get the results you expect for project 1

Bisection mode:
set runmode to 1 and you enable bisection mode,
after listing all valuse it will start to try and converge onto a population 
Each iteration it will print the value it just checked and how close 
that value was to the lower bound

RTR mode:
set runmode to 2 and you enable this mode,
Uses restricted tourny replacement. 

RTR Bisection mode:
set runmode to 3 and you enable this mode,
Uses restricted tourny replacement in bisection. 


### 
In short 
just use ./p3.py to run, you can specify a settings file, or edit the variables 
at the beginning of the file

### Important files 
p3.py: main program
DiversityPreseravtion.py: called from main for RTR
Fitness.py: holds fitness functions
Generational.py: called from main for running Generational models
player.py: the "individual" class
Recombination.py: recombination operators
P3Experiments.pdf: my report portion of this


