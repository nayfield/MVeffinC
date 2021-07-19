#!/usr/bin/env python

import requests
import json

def rip_js_var(blob, varname):
    ss = 'var ' + varname +' ='
    for ln in blob.splitlines():
        if ln.lstrip().startswith(ss):
            return ln.split(ss)[1].rstrip(';')

#########################################################################
# Things to set
#########################################################################

# Remove No Appointments from output (False for debugging)
rmempty = True

# Only consider a certain list of locations (False for statewide)
# onlylook = [186, 195]
onlylook = False

# Which URL to use.  This is for Initial Permit 
theurl = 'https://telegov.njportal.com/njmvc/AppointmentWizard/15'

#########################################################################
# Do the work
#########################################################################
r = requests.get(theurl)
times = json.loads(rip_js_var(r.text, 'timeData'))

# We have what we want, but let's do better
# 1. Enhance times with location names
locs  = json.loads(rip_js_var(r.text, 'locationData'))
loc_table = {}
for l in locs:
    loc_table[l['Id']] = l['Name']
for t in times:
    t['LN'] = loc_table[t['LocationId']]

# 2. remove No Appointments from output
if rmempty:
    times = [x for x in times if not x['FirstOpenSlot'].startswith('No Appointments')]

# 3. restrict to preferred locations if set
if onlylook:
    times = [x for x in times if x['LocationId'] in onlylook]


# Ok print out what we found
for t in times:
    print(t['LN'], ':', t['FirstOpenSlot'])

