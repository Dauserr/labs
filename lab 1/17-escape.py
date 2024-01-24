#txt = "We are the so-called "Vikings" from the north." !!! wrong!!!

##
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
##
txt = "We are the so-called \'Vikings\' from the north."
print(txt)
##
txt = "We are the so-called \\Vikings\\ from the north."
print(txt)
##
txt = "We are the so-called \nVikings from the north."
print(txt)
##
txt = "We are the so-called Vikings from \rthe north." # replaces strig after \r to the beginning
print(txt)
##
txt = "We are the so-called \t Vikings from the north." # tab
print(txt)
##
txt = "We are the so-called \bVikings from the north." # backspace
print(txt)
##
txt = "We are the so-called        \fVikings from the north."
print(txt)
##
txt = "\110\145\154\154\157" # octal to letter
print(txt)
##
txt = "\x48\x65\x6c\x6c\x6f" # hex to letter
print(txt)
##
