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