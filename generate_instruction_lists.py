#!/usr/bin/env python3
import random,os,time

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
\\itemsep0pt"""

latexfinish = """\\end{enumerate}
\\end{multicols}
\\end{document}"""

participants = 16  # maximum number of participants
bias = 2           # twice as likely to go forward than back.
maxsteps = 48      # maximum number of steps your willing to take
tiles = 10         # desired number of tiles: keep drawing instructions until the activity finished in 48 steps.

trials = 0
while True:
    trials = trials + 1
    minmaxpos = 10000
    for n in range(1, 1+participants):
        filenamebase = "random%02d"%n
        filename = filenamebase+".tex"
        pos = 1
        maxpos = 1
        with open(filename,"w") as f:
            print (latexstart, file=f)
            for i in range(maxsteps):
                if random.randint(1, 1+bias)==1:
                    if pos > 1:
                        pos = pos -1
                        print ("\\item\\fbox{Go Back %d}\\\\"%pos, file=f)
                    else:
                        print ("\\item\\fbox{Stay %d}\\\\"%pos, file=f)
                else:
                    pos = pos + 1
                    print ("\\item\\fbox{Go Forward %d}\\\\"%pos, file=f)
                if pos > maxpos:
                    maxpos = pos
            print (latexfinish, file=f)
            if minmaxpos > maxpos:
                minmaxpos = maxpos
        os.system("pdflatex "+filename)
        os.remove(filename)
        os.remove(filenamebase+".aux")
        os.remove(filenamebase+".log")
    if minmaxpos >= tiles:
        print ("You can use up to", minmaxpos, "tiles (took",trials,"tries)")
        break
    else:
        print ("************* NOT FINISHED IN 48 STEPS TRIALSING AGAIN ****************")
        time.sleep(1)
        

