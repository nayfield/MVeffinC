# MV*effin*C

## What is this

A super simple script that will tell you if the MVC has appointments

## How does it work

It grabs the webpage and does some icky parsing of javascript.

It's a ten minute hack and if you break it you get to keep the pieces.

All it does is print the locations with appointments when run.

## What does it need

A super standard python.  Needs requests and json, that's all.

## Can I configure it

Yes.  You can change the URL (for a different type of appointment)

You also can also limit your results to a set of location IDs and ignore the rest of the 
state - a central NJ tradition.

## one more hint

cron sends mail when scripts write to stdout.  
That's why this doesn't print anything unless there are results.

