#!/usr/bin/env python

import re
import os.path

import utils
from rename_argparse import rename_argparse

remove_track_resub = [re.compile(r"\d+ - "),""]
def remove_track(path):
    head, bname = os.path.split(path)
    new_bname = utils.resub(remove_track_resub, bname)
    return os.path.join(head, new_bname)

if __name__ == '__main__':

    rename_argparse(
        remove_track,
        description="remove track numbers from songs in the format \"^\d - .\""
        epilog="""EXAMPLES

    %(f)s "01 - title.mp3" "1 - title.mp3"
    #dry run
    #renames to:
    #  title.mp3
    #  title.mp3

    %(f)s -D "01 - title.mp3" "1 - title.mp3"
    #not Dry run
""")