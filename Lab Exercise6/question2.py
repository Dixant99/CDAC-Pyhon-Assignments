n=input(r"enter the raw PATH: ")
from mymod import countLines
countLines(n)

from mymod import countChars
countChars(n)

from mymod import test
test(n)

print("\nusing from module import all now\n")

from mymod import *
countLines(n)
countChars(n)
test(n)
