# command_line_text_editor
A python text editor based on while loop, able to write programs and execute them
First, write the your file path in the first input Then, press Enter. When you finished writing, write @quit on the last line. You will have a menu, choose the integer before the text.

Some useful commands.

##copy##
copy a line content to another one.
line1number @copy line2number: copy line1 content to line2. 
before 
1- Python is good 
2- C is better 
3- 1 @copy 2 
after 
1- Python is good 
2- Python is good

##swap##
swap two lines contents.
line1number @swap line2number: swap line1 content with line2. 
before 
1- Python is good 
2- C is better 

3- 1 @swap 2 
after 
1- C is better 
2- Python is good

##remove##
remove the line
@remove line1number
before 
1- Python is good 
2- C is better 
3- @remove 2 
after 
1- Python is good

##insert##
insert an input at a specified line.
@insert linenumber input

##blank##
Insert a blank line
@blank linenumber


===Update===
Now you can do regex replacement
Function start with a R and take a regex as argument instead of linenumber.

@Replace regex
prompt for each match and replace it in content tab.

@Replace a regex
prompt once, then replace all matches by the replacement given.


=Looper=
Looper is the command to repeat the same operation on multiple lines. Syntax:
@looper range command
range syntax: startline-endline(inclusive)

##replace##
@looper start-end replace
This will display a prompt 
After all the lines between the range will be replaced by your input.

##copy##
@looper start-end  linenumber-copy
line will be copied to lines between the range.

##swap##
@looper start-end linenumber-swap
line will be swaped with every line.
In the end it will go to the last line.
I'm planning a reverse swap for the first line.

##insert##
@looper start-end insert-inputtoinsert
insert your input on the lines between the range.
If your input have spaces, replace them by underscore. Otherwise it will trick the split function in sperating your input.

##remove##
@looper start-end remove
Remove the lines between the range.
