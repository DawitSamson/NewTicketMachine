# NewTicketMachine
* Ticket Machine Exercise
This device asks you what activity you've come to complete and gives you a turn number based
on the activity you chose.
In this example, you are going to design it for a drugstore that focuses on perfumery,
pharmaceuticals, and cosmetics.
* Your program will ask the consumer which of the places they wish to visit, and depending on the
area they choose, it will assign them a relevant turn number.
* For example:
If I select cosmetics, it will return the letter C (as in cosmetics), - (hiphen) 54.
Following that, it will ask us if we want to take another number to simulate the arrival of a new
client, and the process will be repeated.
Some things to keep in mind.
Customers will take different numbers for different areas (perfumes, medicine, cosmetics) in
different orders, so the system must keep track of how many numbers it has given for each of
those areas and produce the next number for each as they request it.
You probably already realize that we need to use generators and their efficiency to accomplish
this.
The message in which we inform the customer that they are waiting for a number should include
some additional text before and after the number.
* For example:
"Your number is...", then the number with the letter at the beginning, followed by a statement like
"Please wait and someone will assist you shortly."
To avoid having our code repeat itself, instead of putting this text in each of the functions that
calculate the numbers, we can use the decorators' flexibility to create that additional text only
once and then wrap it around any of our functions.
* Finally, you should take advantage of the fact that you now understand how to divide your
program into modules and divide the code into two parts: On the one hand, there is a module
called numbers.py, where you write all the generators and the decorator, and a second
module called main.py, where you write the functions that manage the program's operation.
(For example, instructions to select an area and determine whether the program will keep taking
new clients or end)
Remember what you've learned, and you will succeed.



* when you make this project use main file
