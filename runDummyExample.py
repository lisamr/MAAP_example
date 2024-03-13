# code called in the run.sh script
# runs code in dummyExample.py with arguments passed in from the run.sh script

import os
import argparse
import dummyExample

if __name__ == "__main__":

    # make parser, add arguments, then parse 
    # these arguments get read in through the params string in maap.submitJob(..., **params)
    parser = argparse.ArgumentParser()
    parser.add_argument("--love", type=str)
    parser.add_argument("--hate", type=str)
    args = parser.parse_args()

    dummyExample.run_example(args.love, args.hate)