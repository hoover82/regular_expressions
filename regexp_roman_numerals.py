
## ###############################################################
##
##  Calculate values of Roman Numerals using Regular Expressions
##  Dan Stober
##  2018/03/04
##
## ###############################################################


import re, math

#romanNumeral = 'MCMLXIV'
romanNumeral = 'MDCCLXXVI'
#romanNumeral = 'MMXVIII'


roman_digits = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
minus_values = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
negative_pattern = 'IV|IX|XL|XC|CD|CM'

#Find all occurences of negative combinations and writes them to f
f= re.findall ( negative_pattern, romanNumeral )

#The next two statements remove any matches of the negative combinations from the string
p = re.compile ( negative_pattern )
romanNumeral =  p.sub ( '', romanNumeral )

#Nested dictionary comprehensions that extract the value of each character remaining in the
#  string and the value of each combination found in the string. each of these looked up
#  values are written to a tuple, then the fsum function sums the alements from the two tuples

value  = ( math.fsum([roman_digits[i] for i in romanNumeral])
         + math.fsum([ minus_values[i] for i in f] ) )

print (value)

print ("ALL DONE")
