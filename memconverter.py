#!/usr/bin/env python
MB = 1024*1024
MW = 8e6

def MW2MB(mw):
  return mw * MW / MB

def MB2MW(mb):
  return mb * MB / MW

def GB2MW(gb):
  return MB2MW(gb*1024)

method = 0

print "1\tMW to MB"
print "2\tMB to MW"
print "3\tGB to MW"
print "0\tExit"
method = input("Choose a method: ")

if(method == 0):
  print "done"
elif (method == 1):
   size = input("Enter memory in MW: ")
   print "MBYTES=%i" % (int(MW2MB(size)))
elif (method == 2):
   size = input("Enter memory in MB: ")
   print "MWORDS=%i" % (int(MB2MW(size)))
elif (method == 3):
   size = input("Enter memory in GB: ")
   print "MWORDS=%i" % (int(GB2MW(size)))
else:
  print "Wrong choice of method..."
