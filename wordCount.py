import re
import sys
import os

# set input and output files
if len(sys.argv) is not 3:
    print("Correct usage: wordCount.py <input text file> <output file>")
    exit()

inputFname = sys.argv[1]
outputFname = sys.argv[2]

# first check to make sure program exists
if not os.path.exists("wordCount.py"):
    print("wordCount.py doesn't exist! Exiting")
    exit()

# make sure text files exist
if not os.path.exists(inputFname):
    print("text file input %s doesn't exist! Exiting" % inputFname)
    exit()

# make sure output file exists
if not os.path.exists(outputFname):
    print("wordCount output file %s doesn't exist! Exiting" % outputFname)
    exit()

d = {}
file = open(inputFname)
#Reads file line by line
for x in file:
  #removes punctuation
  line = re.sub(r'[^\w\s]', '', x.lower())
  #splits line to a list
  list = line.split()
  for i in list:
      #if word is in dict add 1 to value else add word to dic
      if i in d.keys():
          d[i]+= 1
      else:
          d[i.lower()] = 1
#Sort dic by value
d = sorted(d.items(), key=lambda x: x[1])
out = open(outputFname, "w")
for i in d:
    s = str(i)
    s = re.sub(r'[^\w\s]', '', s)
    s = s+"\n"
    out.write(s)




