import os
from nltk import edit_distance as leven
import numpy as np
import shutil


WDIR = r'F:\Greys'
FORMAT = 'ION'
LANG = "english"
IFMATCH = 1

ENC = 'utf_8_sig'  # UTF with BOM (starts with an identifier string)
BOM = True
CRLF = True


if FORMAT == 'ION':
    subdir = os.path.join(WDIR, 'Subs')

KEYS = [k for k in os.listdir(subdir) if os.path.isdir(os.path.join(subdir, k))]

for k in KEYS:
    SUBS = [s for s in os.listdir(os.path.join(subdir, k))]
    LSUBS = np.array([leven(s.lower(), LANG) for s in SUBS])  # Identify correct lang for subs

    best = np.min(LSUBS)
    howmany = LSUBS == best
    best = np.array(SUBS)[howmany][IFMATCH - 1]

    base = best.split('.')[-1]
    print(k)

    if (not BOM) and (not CRLF):  # Old version: just copy and rename subtitles
        shutil.copy(os.path.join(subdir, k, best),
                    os.path.join(WDIR, '.'.join([k, base])))
    elif BOM and CRLF:  # Phillips compatible: Inserts BOM string and converts LINUX \n to WIN \r\n
        with open(os.path.join(WDIR, '.'.join([k, base])), 'wb') as wf:  # Open new srt for writing
            with open(os.path.join(subdir, k, best),  # Open selected sub
                      mode='r') as rf:
                wf.write(rf.read().replace('\n', '\r\n').encode(ENC))

print("w")
