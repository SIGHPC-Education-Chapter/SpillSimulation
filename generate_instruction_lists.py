#!/usr/bin/env python3

import random,os,time

# Parameters

participants = 16  # maximum number of participants
bias = 2           # twice as likely to go forward than back.
maxsteps = 48      # maximum number of steps your willing to take
tiles = 10         # desired number of tiles: keep drawing instructions until the activity finished in 48 steps.

# Find instructions that finish

minmaxpos = 0
while minmaxpos < tiles:
    print ("************* DRAWING INSTRUCTIONS ****************")
    instructions = [[] for i in range(participants)]
    minmaxpos = 10000
    for n in range(participants):
        pos = 1
        maxpos = 1
        for i in range(maxsteps):
            if random.randint(1, 1+bias)==1:
                if pos > 1:
                    pos = pos -1
                    instructions[n].append("Go Back")
                else:
                    instructions[n].append("Stay")
            else:
                pos = pos + 1
                instructions[n].append("Go Forward")
            maxpos = max(maxpos, pos)    
        minmaxpos = min(minmaxpos, maxpos)


# Write instructions that finish
        
print ("************** GENERATING PDF INSTRUCTIONS *******************")

latexstart = """\\documentclass[10pt]{article}
\\usepackage{fullpage}
\\usepackage{charter}
\\pagestyle{empty}
\\usepackage{multicol}
\\begin{document}
\\begin{multicols}{3}
\\noindent
\\Large
\\begin{enumerate}
\\itemsep18pt"""

latexsep = """\\end{enumerate}
\\newpage
\\begin{enumerate}
\\itemsep18pt"""

latexfinish = """\\end{enumerate}
\\end{multicols}
\\end{document}"""

filenamebase = "randomall"
filename = filenamebase + ".tex"
with open(filename,"w") as f:
    print (latexstart, file=f)
    for n in range(participants):
        for i in range(maxsteps):
            print ("\\item\\fbox{%s}"%instructions[n][i], file=f)
        if n < participants-1:
            print (latexsep, file=f)   
    print (latexfinish, file=f)
os.system("pdflatex "+filename)
os.remove(filename)
os.remove(filenamebase+".aux")
os.remove(filenamebase+".log")


print ("You can use up to", minmaxpos, "tiles.")        
