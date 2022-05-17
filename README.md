<h1> Welcome to IOET solution </h1>

This project calculates the payment of each employee by the hours they worked in the week having in consideration the different rates of each day and hour.

We used classes, lists, loops, the datetime module and Python's built-in functions.

The main function receives a TXT file having in each line the employee's work week data. An example of a line would be: 'RENE=MO10:00-12:00,TU09:00-12:00,TH01:00-07:00,SA11:00-19:00,SU20:00-21:00'. Then the function splits the data by days and then by hours, calculating each hour rate and appending it into a list. Finally, it sums all the hours-worked rates and writes the result as a line such as 'RENE has to charge: 420USD'.

We are considering the proper format for the days input, raising a value error if its wrong. Then checking that the start hour inputted isn't greater than the end hour, and finally we check that the sums are correct. We checked this with the help of the unittest module.

For running the program, it isn't required any instalation apart from python, because no external libraries or packages were used. It is important to have the data and result txts in the same directory as the main.py file and name them as 'data.txt' and 'result.txt'. Else, the path in the open files functions should be changed.
