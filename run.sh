#!/bin/bash

basedir=$( cd "$(dirname "$0")"; pwd -P )

# this is how you'd specify the environment if you didn't have build.sh
# source activate path/to/your/environment (e.g. /opt/conda/envs/env-feds-dask)

# change the dest to /output on DPS
python ${basedir}/runDummyExample.py --love="$1" --hate="$2"