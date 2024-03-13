# dummy example demonstrating how to submit MAAP job externally
# code requirements: takes inputs, applies code, and creates outputs that will be stored in MAAP's S3 bucket

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