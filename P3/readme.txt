This Version comes with two modes which are selected using the runmode command. 

Generational mode: 
set runmode to 0 and you should get the results you expect for project 1

Bisection mode:
set runmode to 1 and you enable bisection mode,
after listing all valuse it will start to try and converge onto a population 
Each iteration it will print the value it just checked and how close 
that value was to the lower bound

when the values are 5% appart we break and print the values of the string size, and the population 
we found to work for it. 
The population can be inconsistant but it would take to long to get a good average for 
larger problems.  

I also added a small graphing option, the flag is only avalible in the main program (p2.py), 
set graphing = True for it to graph your bisection results. 

also added pauseAtBeginning to check variables before running to make sure things were 
setting properly. 


### 
In short 
just use ./p2.py to run, you can specify a settings file, or edit the variables 
at the beginning of the file

### Important files 
p2.py: main program
Bisection.py: called from main for bisection
Fitness.py: holds fitness functions
Generational.py: called from main for running Generational models
player.py: the "individual" class
Recombination.py: recombination operators
GAP2.pdf: my report portion of this


