#!/bin/bash

export PATH="/<home_directory>/anaconda2/bin:$PATH"
cd /<home_directory>/MGR-Project-Code/

python run_on_server.py Settings/sample_settings_description_file.py $PBS_JOBID

