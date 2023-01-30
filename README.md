




====New version in master branch====

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
@insert input linenumber
Due to the fact that the function split the line by spaces, if your input have many words, replace spaces by underscores.


@insert +i linenumber
Display a prompt to insert your input.
Delete the need to replace the spaces with underscore.



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

linenumber @to destinationline
move a line to a specified line.
The line is inserted at the new emplacement and removed from its old place.

@ponctuate character -b linenumber
Put the character before the line, for example comments in python code: @ponctuate # -b ln.
@ponctuate character -a linenumber
Put the character after the line, for example colon in C code: @ponctuate : -a ln.


@indent tabsize linenumber
indent the line with specified number of tabs.

@indent _ spacesize linenumber
indent the line zith specified number of spaces (no space between _ and spacesize).

@indent ?t linenumber
Get the tab indent size of the line.

@indent ? linenumber
Get the space indent size of the line.


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

@looper start-end insert-+i
Same as above, but display a prompt for input.
Like the standard version, this delete the need of underscores in your input.

@looper start-end insert-startline-+r
Insert a range of line at a line location. The first line is inserted before the startline, then the others lines follow, sending the startline at the bottom of the range.

@looper start-end rangeinsert
Insert lines at a range, with a prompt for each input. Like above, the startline will go at the bottom of the range.

@looper start-0 rangeinsert
Do the same as the previous command, but now the inputs are unlimited. You can insert how many lines you want, then type stop on the last input to end the process.

##remove##
@looper start-end remove
Remove the lines between the range.
