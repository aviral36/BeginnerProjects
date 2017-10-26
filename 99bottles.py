#99 Bottles

#A program that prints out every line to the song 99 bottles of beer on the wall.
#Using built-in python functions.

bottles=99
while bottles>1:
  print bottles, "bottles of beer on the wall,", bottles, "bottles of beer on the wall,\n", "Take one down and pass it around,", bottles-1, "bottles of beer on the wall."
  bottles=bottles-1
print "1 bottle of beer on the wall, 1 bottle of beer.\n Take one down and pass it around, no more bottles of beer on the wall.\n No more bottles of beer on the wall, no more bottles of beer.\n Go to the store and buy some more, 99 bottles of beer on the wall."
