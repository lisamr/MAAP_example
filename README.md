# How to submit a job on MAAP

You have code you want to run on NASA MAAP. You can run it interactively on the ADE or you can submit jobs through DPS. This repo goes over how to submit a job in DPS. 

## Steps
1. **Develop code** 

    I wrote a python function that makes the statment, "I love ____ and I hate ____", and write it to a text file. When you submit a job, you fill in the two blanks. This example is a template demonstrating how parameters can be included and how to create outputs. 
    
    Note that `runDummyExample.py` and `dummyExample.py` are very similar except that the former has extra bits in there to parse arguments that come in from the MAAP API package. I could just put all the code from `dummyExample.py` into `runDummyExample.py`, but I think this better represents how I'd create source code in other scripts and have a designated run script. 

2. **Build shell scripts**

    - `run.sh`: specifies what script gets executed and how the parameter dictionary gets split up
    - `build.sh`: builds environment to run code. If MAAP already has a build environment, you can specify that in `run.sh`(see line 5-6).  
    

3.  **Specify `algorithm_config.yml`**

    Check out `algorithm_config.yml` for how to register your algorithm. This file specifies the repo to pull from, how it's going to run (`run.sh`), parameters involved, etc.

4. **Register your algorithm**

    Register your algorithm on MAAP. Check out `register_algo.ipynb` for how to do it. This opens the MAAP API package, reads in the `.yml` file above, and registers it. In response, an image gets created and you should be able to submit jobs. 

    Whenever anything changes to your setup--python code, input parameters, environment--you need to reregister.  

5. **Submit job**

    `submit_job.ipynb` submits your job to MAAP and the outputs should exist there.




## My remaining questions
- In `algorithm_config.yml`, how do I know what the `docker_container_url` should be? 
- How do I get the path to my private bucket? Right now, the output directory is set to 'test_output'. 
- [This script](https://repo.maap-project.org/gcorradini/fireatlas_nrt/-/blob/conus-dps/maap_runtime/submit-dps-job.py) defines `submit_job`, which is just a wrapper for `maap.submitJob()`. Why? And I searched for where this script gets called and couldn't find it.
    