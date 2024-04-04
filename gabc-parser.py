import re

#I need to find how to enable special characters
#This title is great!  I can use the first two letters to identify the genre, and the keyword "vatican" to avoid repeats - I only wish the title itself contained the mode.  I could use readline for that.
input = open("an--exsultabunt_domino--solesmes_1934.gabc", "r")
# it appears this code editor doesnt like diacritics, but those are somewhat important to me
# start with the frequency of pitches

header = re.search(".\%\%", gabc_file)
#shear off % signs
clef = re.search("\%\%\n\((c|f)(4|3|2))", gabc_file)
#shear off % signs
body = re.search("\%\%\n\((c|f)(4|3|2)).", gabc_file)
#shear off % signs and clef

syllablePitches =

def split_gabc(str gabc_file):
    header = re.search(".\%\%", gabc_file)
    
    clef = re.search("\%\%\n\((c|f)(4|3|2))", gabc_file)
    
    body = re.search("\%\%\n\((c|f)(4|3|2)).", gabc_file)
    
    return split_gabc_file[header, clef, body]

#test function
print(split_gabc(input))

def extract_metadata(str header):
    return metadata[usage, title, mode, occasion]

def extract_note_positions

def convert_positions_to_pitches

