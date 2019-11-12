# SpillSimulation

Simulate a chemical spill in a river using people as "chemicals"

## Extended Description

Participants (can be volunteers from a larger audience) are the chemicals in the spill.  Tiles
are laid out in a line on the floor to represent the
river. The first tile is where the "chemicals" enter the river. The last
tile is a larger river, a lake, the sea, or the ocean (call it
whatever is locally appropriate).

Each "chemical" gets their own numbered list of what to do in
each step, which is either "Go Forward" (i.e., downstream towards
the lake/sea/ocean), "Stay", and "Go Back" (i.e. upstream, towards the
source of the spill).  It should be more likely to go downstream than
upstream.

The moderator should call out the step numbers, and have the
"chemicals" do their own instruction for that step at the same time.

If a "chemical" reaches the lake, that "chemical" stops, but the others continue.

The question to answer is: how many steps does it takes for the river
to be drained of all chemicals?

Optionally, discuss afterwards:

  - why you'd want to do this with computers if you can do it with
    people?

  - what would be the effect if in our simulation, we could only move
    one chemicals at a time?


## Pre-Requisites

Reading.

## Concepts

Algorithms, randomness, simulations, parallel processing

## Learning Outcomes

Understand what simulations do and why you'd
have computers do them.

## Equipment

Print out the per-chemical instructions generated by the python script
included in this repo.  These instructions are randomly drawn such
that it is two times more likely to go downstream than upstream, 16
sets of instructions are generated, such that they all leave a river
of 10 tiles in at most 48 steps. The script uses pdflatex and is written in
python3.

For the tiles, you can really use anything. Mark the first tile with
"Start" and the last with "Finish".  Lay parallel tracks of tiles for
larger groups of participants.

## Group Size

Between 3 and 16 is probably ideal.

## Duration

Approximately 15-20 minutes.

## Tips

  - The process is slower than you'd imagine.  Be conservative in the
    number of tiles; a river length of 6 to 8 tiles is more
    than sufficient.

  - It can help to start the activity first with one participant as an
    example (e.g. one of the older kids), then include the
    others, especially if you have a lot of so participants, or if
    they are very young.
  
  - Setup the tiles with plenty of space to accommodate anybody.

  - Although tiles can be made of anything, if you can have something
    that stays in place better than a piece of paper, that's always a
    good idea.  
    
  - It can be helpful to have the forward direction indicated by an arrow on the tiles.

  - Unfortunately, there always seems to be some recent event to which
    you can related this activity.  E.g., just on November 11th, 2019,
    there was a diesel spill in the Blue River, a tributary of the
    Colorado River, just 80 miles west of Denver:
    https://denver.cbslocal.com/2019/11/11/truck-spills-fuel-breckenridge-sliding-off-icy-road-blue-river/


## Contact

Ramses van Zon - rzon@scinet.utoronto.ca
