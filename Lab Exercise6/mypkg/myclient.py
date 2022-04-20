"""QUESTION4"""
import mymod
n=input(r"Enter the PATH:")
print("--test function countLines--")
mymod.countLines(n)
print("--test function countChars--")
mymod.countChars(n)
print("--test function test--")
mymod.test(n)

print("\nusing from to import\n")

from mymod import countLines,countChars,test
countLines(n)
print()
countChars(n)
print()
test(n)

print(dir())
