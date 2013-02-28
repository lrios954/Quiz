#!/usr/bin/ python
#encoding: UTF-8
import sys, codecs
import numpy as np
#opens file with the right encoding and read everything
filein = codecs.open(sys.argv[1], "r", "utf8") 
fullin = filein.read()
fulltext = fullin.lower() #make everything lower case
filein.close()

#this is the list of different characters
all_characters = list(set(fulltext))

# a list of charachters to remove from the all_characters list
to_remove = [' ', ',', '_', '.','(', ')', '#','"','[',']','\n', '\r', u'\x0c',u'\u011d', u'\u2014', u'\u016d', u'\u0109', u'\u2123']

for undesired in to_remove:
    try:
        all_characters.remove(undesired) #if undesired is not in the list, remove fails
    except:
        pass

#count the number of times in the text
frequencies = []
for valid in all_characters:
    n_times = 1.0 * fulltext.count(valid)
    frequencies.append(n_times)

#make a final list of frequencies and charachters
n_total = sum(frequencies)
final_list = []
for frequencies, letter in zip(frequencies, all_characters):
    final_list.append((frequencies/n_total, letter))

#sort it
final_list.sort()
final_list.reverse()
#
#
#

#write it to a file, the new exit is only frecuences
fileout = codecs.open("frecuencias"+sys.argv[1], "w", "utf8") 
for item in final_list:
    fileout.write("%f\n"%(item[0]))
    
filein.close()  


#opens a file with only frecuences
filein = codecs.open("frecuencias"+sys.argv[1], "r", "utf8") 
frec = np.loadtxt("frecuencias"+sys.argv[1])


r=np.arange(20)+1

m=np.polyfit(log(r), log(frec), 1)
    
k=m[0]
    
    
#output 
fileout = codecs.open("coeficiente de "+sys.argv[1], "w", "utf8") 
for i in range(20):
    fileout.write("%s %f\n"%(sys.argv[1], k))